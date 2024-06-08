import json
import uuid
import redis 
import os
import yaml
r = redis.Redis(host=os.environ['REDIS_HOST'], port=int(os.environ['REDIS_PORT']), decode_responses=True)
# used ports are stored in redis
def get_not_allocated_port():
    low_port = 0
    high_port = 0
    if os.environ['LOW_PORT'] and os.environ['HIGH_PORT']:
        low_port = int(os.environ['LOW_PORT'])
        high_port = int(os.environ['HIGH_PORT'])
    else:
        low_port = 40000
        high_port = 50000
    for i in range(low_port, high_port+1):
        if not r.get(str(i)):
            return i
def allocate_port(port):
    r.set(str(port), 'allocated')
def deallocate_port(port):
    r.delete(str(port))
def generate_manifest_from_template(name, image, port):
    data = {}
    service_manifest = {}
    namespace_manifest = {}
    with open('manifests/manifest_template.yaml', 'r') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    with open('manifests/service_manifest.yaml', 'r') as f:
        service_manifest = yaml.load(f, Loader=yaml.FullLoader)
    with open('manifests/namespace_manifest.yaml', 'r') as f:
        namespace_manifest = yaml.load(f, Loader=yaml.FullLoader)
    uuid_namespace = name + '-' + str(uuid.uuid4())[:8]
    data['metadata']['name'] = name
    data['metadata']['namespace'] = uuid_namespace
    service_manifest['metadata']['name'] = name
    service_manifest['metadata']['namespace'] = uuid_namespace
    namespace_manifest['metadata']['name'] = uuid_namespace

    # data['name'] = name
    # data['image'] = image
    # data['ports'] = port
    target_port = get_not_allocated_port()
    allocate_port(target_port)
    service_manifest['spec']['ports'][0]['targetPort'] = target_port
    service_manifest['spec']['ports'][0]['port'] = port
    service_manifest['spec']['selector']['app'] = name
    return (data, service_manifest, namespace_manifest)
    

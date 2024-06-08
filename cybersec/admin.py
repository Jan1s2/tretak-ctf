from django.contrib import admin
from .models import Cve, Category, Challenge, Exploit, Cwe

# Register your models here.
admin.site.register(Cve)
admin.site.register(Category)
admin.site.register(Challenge)
admin.site.register(Exploit)
admin.site.register(Cwe)


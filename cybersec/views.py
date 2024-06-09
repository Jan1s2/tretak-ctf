from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.http import HttpResponseRedirect, JsonResponse
# Import metody render pro vykreslení šablon
from django.shortcuts import render
from django.urls import reverse_lazy
# Import generických tříd ListView a DetailView z modulu django.views.generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Cve, Cwe, Category, Challenge, Exploit, Flag

# Create your views here.
def index(request):
    context = {
            'categories': Category.objects.all(),
    }
    return render(request, 'index.html', context=context)

def submit_flag(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        flag_id = request.POST.get('flag_id')
        # flag id is challengeid_flagname
        flag_id = flag_id.split('_')
        challenge = Challenge.objects.get(id=flag_id[0])
        valid_flags = Flag.objects.filter(challenge=challenge)
        if flag in [f.flag for f in valid_flags]:
            # flag is valid - return JSON with valid true
            return JsonResponse({'valid': True})
        else:
            # flag is invalid - return JSON with valid false
            return JsonResponse({'valid': False})
    else:
        return HttpResponseRedirect(reverse_lazy('index'))

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    ordering = ['name']
    paginate_by = 10

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    context_object_name = 'category'

class ChallengeDetailView(DetailView):
    model = Challenge
    template_name = 'challenge_detail.html'
    context_object_name = 'challenge'

class CveListView(ListView):
    model = Cve
    template_name = 'cve_list.html'
    context_object_name = 'cves'
    ordering = ['cve_id']
    paginate_by = 10

class CveDetailView(DetailView):
    model = Cve
    template_name = 'cve_detail.html'
    context_object_name = 'cve'

class CweListView(ListView):
    model = Cwe
    template_name = 'cwe_list.html'
    context_object_name = 'cwes'
    ordering = ['cwe_id']
    paginate_by = 10

class CveUpdateView(UpdateView):
    model = Cve
    template_name = 'cve_form.html'
    fields = "__all__"

class CveDeleteView(DeleteView):
    model = Cve
    template_name = 'cve_confirm_delete.html'
    success_url = reverse_lazy('cves')

class CweDetailView(DetailView):
    model = Cwe
    template_name = 'cwe_detail.html'
    context_object_name = 'cwe'
class CweUpdateView(UpdateView):
    model = Cwe
    template_name = 'cwe_form.html'
    fields = "__all__"
class CweDeleteView(DeleteView):
    model = Cwe
    template_name = 'cwe_confirm_delete.html'
    success_url = reverse_lazy('cwes')
class CweCreateView(CreateView):
    model = Cwe
    template_name = 'cwe_form.html'
    fields = "__all__"

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'category_form.html'
    fields = "__all__"

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = "__all__"

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('categories')

class ChallengeCreateView(CreateView):
    model = Challenge
    template_name = 'challenge_form.html'
    fields = "__all__"

class ChallengeUpdateView(UpdateView):
    model = Challenge
    template_name = 'challenge_form.html'
    fields = "__all__"

class ChallengeDeleteView(DeleteView):
    model = Challenge
    template_name = 'challenge_confirm_delete.html'
    success_url = reverse_lazy('challenges')

class CveCreateView(CreateView):
    model = Cve
    template_name = 'cve_form.html'
    fields = "__all__"

class ExploitListView(ListView):
    model = Exploit
    template_name = 'exploit_list.html'
    context_object_name = 'exploits'
    ordering = ['name']
    paginate_by = 10

class ExploitDetailView(DetailView):
    model = Exploit
    template_name = 'exploit_detail.html'
    context_object_name = 'exploit'

class ExploitCreateView(CreateView):
    model = Exploit
    template_name = 'exploit_form.html'
    fields = "__all__"

class ExploitUpdateView(UpdateView):
    model = Exploit
    template_name = 'exploit_form.html'
    fields = "__all__"
class ExploitDeleteView(DeleteView):
    model = Exploit
    template_name = 'exploit_confirm_delete.html'
    success_url = reverse_lazy('exploits')


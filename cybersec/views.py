from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
# Import metody render pro vykreslení šablon
from django.shortcuts import render
from django.urls import reverse_lazy
# Import generických tříd ListView a DetailView z modulu django.views.generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Cve, Cwe, Category, Challenge, Exploit

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html', context=context)

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


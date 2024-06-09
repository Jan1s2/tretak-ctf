from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('cves/', views.CveListView.as_view(), name='cves'),
    path('cve/<int:pk>', views.CveDetailView.as_view(), name='cve-detail'),
    path('cve/create/', views.CveCreateView.as_view(), name='cve_create'),
    path('cve/<int:pk>/update/', views.CveUpdateView.as_view(), name='cve_update'),
    path('cve/<int:pk>/delete/', views.CveDeleteView.as_view(), name='cve_delete'),
    path('cwes/', views.CweListView.as_view(), name='cwe'),
    path('cwe/<int:pk>', views.CweDetailView.as_view(), name='cwe-detail'),
    path('cwe/create/', views.CweCreateView.as_view(), name='cwe_create'),
    path('cwe/<int:pk>/update/', views.CweUpdateView.as_view(), name='cwe_update'),
    path('cwe/<int:pk>/delete/', views.CweDeleteView.as_view(), name='cwe_delete'),
    path('challenge/<int:pk>', views.ChallengeDetailView.as_view(), name='challenge-detail'),
    path('challenge/create/', views.ChallengeCreateView.as_view(), name='challenge_create'),
    path('challenge/<int:pk>/update/', views.ChallengeUpdateView.as_view(), name='challenge_update'),
    path('challenge/<int:pk>/delete/', views.ChallengeDeleteView.as_view(), name='challenge_delete'),
    path('exploits/', views.ExploitListView.as_view(), name='exploits'),
    path('exploit/<int:pk>', views.ExploitDetailView.as_view(), name='exploit-detail'),
    path('exploit/create/', views.ExploitCreateView.as_view(), name='exploit_create'),
    path('exploit/<int:pk>/update/', views.ExploitUpdateView.as_view(), name='exploit_update'),
    path('exploit/<int:pk>/delete/', views.ExploitDeleteView.as_view(), name='exploit_delete'),
    path('flag/submit', views.submit_flag, name='flag_submit'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diseases/', views.disease_list, name='disease_list'),
    path('disease/<slug:slug>/', views.disease_detail, name='disease_detail'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('assessment/', views.self_assessment, name='self_assessment'),
    path('prevention/', views.prevention_guide, name='prevention_guide'),
]
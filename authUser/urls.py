from django.urls import path
from . import views

app_name = 'authUser'

urlpatterns = [
    path('login/', views.login_register_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
]
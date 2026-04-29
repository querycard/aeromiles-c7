from django.urls import path
from . import views

urlpatterns = [
    path('kelola-member/', views.kelola_member, name='kelola_member'),
]
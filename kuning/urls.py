from django.urls import path
from . import views

app_name = 'kuning'

urlpatterns = [
    path('kelola-member/', views.kelola_member, name='kelola_member'),
    path('identitas/', views.identitas_member_view, name='identitas'),
]
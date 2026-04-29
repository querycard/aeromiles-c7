from django.urls import path
from .views import daftar_hadiah, daftar_mitra

urlpatterns = [
    path('manage-rewards/', daftar_hadiah, name='kelola_hadiah'),
    path('partners/', daftar_mitra, name='kelola_mitra'),
]
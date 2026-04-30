from django.urls import path
from . import views

app_name = 'biru'

urlpatterns = [
    path('redeem/', views.redeem_view, name='redeem'),
    path('beli-package/', views.beli_package_view, name='beli_package'),
    path('info-tier/', views.info_tier_view, name='info_tier'),
    path('laporan/', views.laporan_view, name='laporan'),
]
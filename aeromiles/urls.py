from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('auth/', include('authUser.urls')),
    path('biru/', include('biru.urls')),
    path('merah/ ', include('merah.urls')),
    path('hijau/', include('hijau.urls')),
    path('kuning/', include('kuning.urls')), 
]
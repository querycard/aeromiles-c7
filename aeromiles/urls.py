"""
URL configuration for aeromiles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from hijau import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authUser.urls')),

    path('klaim/', views.member_claim_miles, name='claim_miles'),
    
    # Rute Staff
    path('staff/klaim/', views.staff_claim_approval, name='staff_claim_approval'),
    path('staff/klaim/approve/<int:id>/', views.staff_approve_claim, name='staff_approve_claim'),
    path('staff/klaim/reject/<int:id>/', views.staff_reject_claim, name='staff_reject_claim'),

    path('transfer/', views.transfer_miles_view, name='transfer_miles'),

]

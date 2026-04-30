from django.urls import path
from . import views

app_name = 'hijau'

urlpatterns = [
    path('klaim/', views.member_claim_miles, name='claim_miles'),
    
    # Rute Staff
    path('staff/klaim/', views.staff_claim_approval, name='staff_claim_approval'),
    path('staff/klaim/approve/<int:id>/', views.staff_approve_claim, name='staff_approve_claim'),
    path('staff/klaim/reject/<int:id>/', views.staff_reject_claim, name='staff_reject_claim'),

    path('transfer/', views.transfer_miles_view, name='transfer_miles'),
]
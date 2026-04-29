from django.shortcuts import render

# Create your views here.
def login_register_view(request):
    return render(request, 'login_register.html')

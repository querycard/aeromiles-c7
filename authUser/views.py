from django.shortcuts import redirect, render

# Create your views here.
def login_register_view(request):
    if request.method == 'POST':
        # Langsung bypass / lempar ke halaman kelola member
        return redirect('kelola_member') 
        
    return render(request, 'login_register.html')
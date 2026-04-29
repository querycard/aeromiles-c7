from django.shortcuts import render

def kelola_member(request):
    # Ini data user bohongan buat ngetes navbar
    dummy_user = {
        'is_authenticated': True, 
        'role': 'member', 
        'get_nama_lengkap': 'Khansa Dinda' 
    }
    
    # Kirim dummy_user tadi dengan nama 'current_user' agar terbaca oleh navbar.html
    return render(request, 'kelola_member.html', {'current_user': dummy_user})
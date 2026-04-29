from django.shortcuts import render

def kelola_member(request):
    # Ini data user bohongan buat ngetes navbar
    dummy_user = {
        'is_authenticated': True, 
        'role': 'staff', 
        'get_nama_lengkap': 'Khansa Dinda' 
    }
    
    return render(request, 'kelola_member.html', {'current_user': dummy_user})

def identitas_member_view(request):
    # Simulasi user yang sedang login sebagai Member
    current_user = {
        'is_authenticated': True,
        'role': 'staff', # 
        'get_nama_lengkap': 'Khansa Dinda'
    }
    return render(request, 'identitas_saya.html', {'current_user': current_user})
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.contrib.auth.hashers import make_password, check_password

def login_register_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'register':
            role = request.POST.get('role')
            salutation = request.POST.get('salutation')
            first_mid_name = request.POST.get('first_mid_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('reg_email')
            country_code = request.POST.get('country_code')
            mobile_number = request.POST.get('mobile_number')
            tanggal_lahir = request.POST.get('tanggal_lahir')
            kewarganegaraan = request.POST.get('kewarganegaraan')
            raw_password = request.POST.get('password')
            kode_maskapai = request.POST.get('kode_maskapai')

            
            hashed_password = make_password(raw_password)

            try:
                with connection.cursor() as cursor:
                    
                    cursor.execute("""
                        INSERT INTO aeromiles.PENGGUNA 
                        (email, password, salutation, first_mid_name, last_name, country_code, mobile_number, tanggal_lahir, kewarganegaraan)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, [email, hashed_password, salutation, first_mid_name, last_name, country_code, mobile_number, tanggal_lahir, kewarganegaraan])

                    
                    if role == 'Member':
                        
                        cursor.execute("""
                            INSERT INTO aeromiles.MEMBER (email, tanggal_bergabung, id_tier, award_miles, total_miles)
                            VALUES (%s, CURRENT_DATE, 'T001', 0, 0)
                        """, [email])
                    
                    elif role == 'Staf':
                        cursor.execute("""
                            INSERT INTO aeromiles.STAF (email, kode_maskapai)
                            VALUES (%s, %s)
                        """, [email, kode_maskapai])

                
                messages.success(request, f"Registrasi {role} berhasil! Silakan Login.")
            except Exception as e:
                
                messages.error(request, f"Gagal mendaftar: Email mungkin sudah terdaftar.")
            
            return redirect('authUser:login')

        elif action == 'login':
            email = request.POST.get('email')
            raw_password = request.POST.get('password')

            with connection.cursor() as cursor:
                
                cursor.execute("SELECT password FROM aeromiles.PENGGUNA WHERE email = %s", [email])
                row = cursor.fetchone()

            
            if row and check_password(raw_password, row[0]):
                request.session['email'] = email
                
                with connection.cursor() as cursor:
                    cursor.execute("SELECT email FROM aeromiles.MEMBER WHERE email = %s", [email])
                    if cursor.fetchone():
                        request.session['role'] = 'Member'
                    else:
                        request.session['role'] = 'Staf'
                
                messages.success(request, f"Login berhasil! Selamat datang.")
                return redirect('authUser:dashboard')
                
                
            else:
                messages.error(request, "Email atau password salah!")  
            return redirect('authUser:login')

    return render(request, 'login_register.html')

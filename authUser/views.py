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

            
            if row and (raw_password == row[0] or check_password(raw_password, row[0])):
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

def dashboard_view(request):
    email = request.session.get('email')
    role = request.session.get('role')
    
    if not email:
        return redirect('authUser:login')

    data = {}
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT salutation, first_mid_name, last_name, email, country_code, mobile_number, kewarganegaraan, tanggal_lahir 
            FROM aeromiles.PENGGUNA WHERE email = %s
        """, [email])
        user_row = cursor.fetchone()
        
        if user_row:
            data = {
                'nama_lengkap': f"{user_row[0]} {user_row[1]} {user_row[2]}",
                'email': user_row[3],
                'telepon': f"{user_row[4]} {user_row[5]}",
                'kewarganegaraan': user_row[6],
                'tanggal_lahir': user_row[7],
                'role': role
            }

        if role == 'Member':
            cursor.execute("""
                SELECT nomor_member, id_tier, total_miles, award_miles, tanggal_bergabung 
                FROM aeromiles.MEMBER WHERE email = %s
            """, [email])
            m_row = cursor.fetchone()
            if m_row:
                data.update({
                    'nomor_member': m_row[0], 'tier': m_row[1], 
                    'total_miles': m_row[2], 'award_miles': m_row[3], 'tanggal_bergabung': m_row[4]
                })
        elif role == 'Staf':
            cursor.execute("SELECT id_staf, kode_maskapai FROM aeromiles.STAF WHERE email = %s", [email])
            s_row = cursor.fetchone()
            if s_row:
                data.update({'id_staf': s_row[0], 'kode_maskapai': s_row[1]})

    return render(request, 'dashboard.html', {'data': data})

def profile_view(request):
    email = request.session.get('email')
    role = request.session.get('role')
    
    if not email:
        return redirect('authUser:login')

    if request.method == 'POST':
        salutation = request.POST.get('salutation')
        first_mid_name = request.POST.get('first_mid_name')
        last_name = request.POST.get('last_name')
        country_code = request.POST.get('country_code')
        mobile_number = request.POST.get('mobile_number')
        kewarganegaraan = request.POST.get('kewarganegaraan')
        tanggal_lahir = request.POST.get('tanggal_lahir')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE aeromiles.PENGGUNA 
                SET salutation=%s, first_mid_name=%s, last_name=%s, country_code=%s, 
                    mobile_number=%s, kewarganegaraan=%s, tanggal_lahir=%s
                WHERE email=%s
            """, [salutation, first_mid_name, last_name, country_code, mobile_number, kewarganegaraan, tanggal_lahir, email])
            
            if role == 'Staf':
                kode_maskapai = request.POST.get('kode_maskapai')
                cursor.execute("UPDATE aeromiles.STAF SET kode_maskapai=%s WHERE email=%s", [kode_maskapai, email])

        messages.success(request, "Profil berhasil diperbarui!")
        return redirect('authUser:profile')

    user_data = {}
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM aeromiles.PENGGUNA WHERE email = %s", [email])
        cols = [col[0] for col in cursor.description]
        user_data = dict(zip(cols, cursor.fetchone()))
        user_data['role'] = role
        
        if role == 'Member':
            cursor.execute("SELECT nomor_member, tanggal_bergabung FROM aeromiles.MEMBER WHERE email = %s", [email])
            m_row = cursor.fetchone()
            user_data['nomor_member'] = m_row[0]
            user_data['tanggal_bergabung'] = m_row[1]
        elif role == 'Staf':
            cursor.execute("SELECT id_staf, kode_maskapai FROM aeromiles.STAF WHERE email = %s", [email])
            s_row = cursor.fetchone()
            user_data['id_staf'] = s_row[0]
            user_data['kode_maskapai'] = s_row[1]

    return render(request, 'profile.html', {'user': user_data})
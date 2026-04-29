from django.shortcuts import render

# Create your views here.
def member_claim_miles(request):
    context = {
        'claims': [],
        'maskapai_list': [],
        'bandara_list': []
    }
    
    return render(request, 'member_claim_miles.html', context)


def staff_claim_approval(request):
    # Dummy data agar tabel terisi dan bisa dites tampilannya
    dummy_claims = [
        {
            'id': 1, 'member_name': 'Budi Santoso', 'member_email': 'budi@example.com',
            'maskapai': 'GA', 'asal': 'CGK', 'tujuan': 'DPS', 
            'tanggal': '25-Apr-2026', 'flight_number': 'GA198', 
            'kelas_kabin': 'Economy', 'status': 'Menunggu'
        },
        {
            'id': 2, 'member_name': 'Siti Aminah', 'member_email': 'siti@example.com',
            'maskapai': 'SQ', 'asal': 'SIN', 'tujuan': 'NRT', 
            'tanggal': '15-Mar-2026', 'flight_number': 'SQ638', 
            'kelas_kabin': 'Business', 'status': 'Disetujui'
        },
        {
            'id': 3, 'member_name': 'Andi Pratama', 'member_email': 'andi@example.com',
            'maskapai': 'JT', 'asal': 'SUB', 'tujuan': 'KUL', 
            'tanggal': '10-Feb-2026', 'flight_number': 'JT281', 
            'kelas_kabin': 'Economy', 'status': 'Ditolak'
        }
    ]
    
    # Data maskapai untuk dropdown filter
    dummy_maskapai = [
        {'kode_maskapai': 'GA'}, 
        {'kode_maskapai': 'SQ'}, 
        {'kode_maskapai': 'JT'}
    ]

    context = {
        'claims': dummy_claims,
        'maskapai_list': dummy_maskapai,
    }
    
    # Pastikan nama file HTML-nya sesuai dengan yang Anda save!
    return render(request, 'staff_claim_miles.html', context)


def staff_approve_claim(request, id):
    if request.method == 'POST':
        # Nanti logika mengubah status di database ditaruh di sini
        # Contoh: ClaimMissingMiles.objects.filter(id=id).update(status='Disetujui')
        print(f"Klaim ID {id} berhasil DISETUJUI!")
        
    # Setelah memproses, kembalikan halaman ke daftar klaim staff
    return redirect('staff_claim_approval')

def staff_reject_claim(request, id):
    if request.method == 'POST':
        # Nanti logika mengubah status di database ditaruh di sini
        # Contoh: ClaimMissingMiles.objects.filter(id=id).update(status='Ditolak')
        print(f"Klaim ID {id} DITOLAK!")
        
    # Setelah memproses, kembalikan halaman ke daftar klaim staff
    return redirect('staff_claim_approval')

def transfer_miles_view(request):
    # Data dummy agar Frontend bisa tampil tanpa harus login
    context = {
        'award_miles': 32000,
        'riwayat_transfer': [
            {
                'timestamp': '2025-01-15 10:30',
                'sender_name': 'Jane Smith', # Simulasi pengirim
                'receiver_name': 'Jane Smith', 
                'receiver_email': 'jane@example.com',
                'amount': 5000,
                'note': 'Hadiah ulang tahun',
                'tipe': 'Kirim',
            },
            {
                'timestamp': '2025-02-01 14:00',
                'sender_name': 'Budi A. Santoso',
                'receiver_email': 'budi@example.com',
                'amount': 2000,
                'note': '-',
                'tipe': 'Terima',
            }
        ],
    }
    return render(request, 'transfer_miles.html', context)
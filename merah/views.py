from django.shortcuts import render

def daftar_hadiah(request):
    # Data dummy untuk Fitur 15: Manajemen Hadiah & Penyedia
    context = {
        'hadiah': [
            {'kode': 'RWD-001', 'nama': 'Tiket Jakarta-Bali', 'miles': 15000, 'penyedia': 'Garuda Indonesia', 'valid': '2026-01-01 s/d 2026-12-31'},
            {'kode': 'RWD-002', 'nama': 'Voucher Hotel Rp500rb', 'miles': 8000, 'penyedia': 'Traveloka', 'valid': '2026-04-01 s/d 2026-10-01'},
        ]
    }
    return render(request, 'kelola_hadiah.html', context)

def daftar_mitra(request):
    # Data dummy untuk Fitur 16: Manajemen Mitra
    context = {
        'mitra': [
            {'email': 'contact@traveloka.com', 'id_penyedia': 6, 'nama': 'Traveloka', 'sejak': '2023-01-15'},
            {'email': 'info@tiket.com', 'id_penyedia': 7, 'nama': 'Tiket.com', 'sejak': '2023-05-20'},
        ]
    }
    return render(request, 'kelola_mitra.html', context)
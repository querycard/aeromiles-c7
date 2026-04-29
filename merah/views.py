from django.shortcuts import render

def daftar_hadiah(request):
    context = {
        'hadiah': [
            {'kode': 'RWD-001', 'nama': 'Tiket Jakarta-Bali', 'miles': 15000, 'penyedia': 'Garuda Indonesia', 'start': '2026-01-01', 'end': '2026-12-31', 'deskripsi': 'Tiket kelas ekonomi.'},
            {'kode': 'RWD-002', 'nama': 'Voucher Hotel 500rb', 'miles': 8000, 'penyedia': 'Traveloka', 'start': '2026-04-01', 'end': '2026-10-01', 'deskripsi': 'Berlaku di semua hotel mitra.'},
        ],
        'penyedia_list': ['Garuda Indonesia', 'AirAsia', 'Traveloka', 'Plaza Premium'] 
    }
    return render(request, 'kelola_hadiah.html', context)

def daftar_mitra(request):
    context = {
        'mitra': [
            {'email': 'partner@traveloka.com', 'id_penyedia': 6, 'nama': 'Traveloka', 'sejak': '2023-01-15'},
            {'email': 'info@tiket.com', 'id_penyedia': 7, 'nama': 'Tiket.com', 'sejak': '2023-05-20'},
        ]
    }
    return render(request, 'kelola_mitra.html', context)
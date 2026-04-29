from django.shortcuts import render

# Create your views here.
def redeem_view(request): return render(request, 'redeem_hadiah.html')
def beli_package_view(request): return render(request, 'beli_package.html')
def info_tier_view(request): return render(request, 'info_tier.html')
def laporan_view(request): return render(request, 'laporan_transaksi.html')
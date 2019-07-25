from django.shortcuts import render, redirect
from .models import Barang
from django.http import Http404
from .forms import InputBarang
# Create your views here.

def home(request):
    home = Barang.objects.all()
    return render(request, 'home.html', {'barangs':home})

def detail(request,barangid):
    try:
        barang_id=Barang.objects.get(pk=barangid)
        deskripsis = barang_id.deskripsi.split(',')
    except Barang.DoesNotExist:
        raise Http404(f"Barang dengan entry nomor {barangid} tidak tersedia.")
    return render(request, 'detail.html', {'barang_id':barang_id,'deskripsis':deskripsis})

def input_barang(request):
    if request.method == "POST":
        form_barang = InputBarang(request.POST)
        if form_barang.is_valid():
            post_barang = form_barang.save(commit=False)
            post_barang.save()
            return redirect('home')
    else:
        form_barang = InputBarang()
    return render(request, 'tambah_barang.html', {'form_barang':form_barang})
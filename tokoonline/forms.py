from django import forms
from .models import Barang

class InputBarang(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ('nama', 'harga', 'deskripsi', 'ketersediaan', 'foto_url')
from django.contrib import admin
from .models import Barang
# Register your models here.
@admin.register(Barang)
class AuthorHewan(admin.ModelAdmin):
    list_display = ('id', 'nama', 'harga', 'deskripsi', 'ketersediaan', 'foto_url')
    list_display_links = ('id', 'nama', 'deskripsi')
    search_fields = ['nama', 'deskripsi']


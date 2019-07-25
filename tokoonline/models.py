from django.db import models

# Create your models here.
class Barang(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.PositiveIntegerField()
    ketersediaan = models.PositiveIntegerField()
    deskripsi = models.TextField(max_length=500)
    foto_url = models.URLField(max_length=100)

# Generated by Django 2.2.3 on 2019-07-25 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('harga', models.PositiveIntegerField()),
                ('ketersediaan', models.PositiveIntegerField()),
                ('deskripsi', models.TextField(max_length=500)),
                ('foto_url', models.URLField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-17 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0003_alter_karyawan_phone'),
        ('usr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='karyawan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pegawai.karyawan'),
        ),
    ]
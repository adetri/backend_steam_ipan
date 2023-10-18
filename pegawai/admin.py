from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(Role)


# class KaryawanAdmin(admin.ModelAdmin):
#     readonly_fields = ('nik',)  # Add the 'nik' field to readonly_fields


admin.site.register(Karyawan)

from django.urls import path, include
from django.contrib import admin
from .views import *
app_name = 'pegawai'

urlpatterns = [
    path('fatch-all-pegawai', fatch_all_pegawai, name='fatch-all-pegawai'),
    path('get-pegawai/<pk>', get_pegawai, name='get_pegawai'),
    path('edit-pegawai/<pk>', edit_pegawai, name='edit_pegawai'),
    path('delete-pegawai/<pk>', delete_pegawai, name='delete_pegawai'),
    path('create-pegawai', create_pegawai, name='create_pegawai'),


    path('fatch-all-role', fatch_all_role, name='fatch_all_role'),
    path('get-role/<pk>', get_role, name='get_role'),
    path('edit-role/<pk>', edit_role, name='edit_role'),
    path('delete-role/<pk>', delete_role, name='delete_role'),
    path('create-role', create_role, name='create_role'),


]

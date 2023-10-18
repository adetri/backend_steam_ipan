from rest_framework import serializers
from .models import *


class KaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = '__all__'


class EditkaryawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = ['name', 'phone', 'role']


class GetRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class GetKaryawanSerializer(serializers.ModelSerializer):
    role = GetRoleSerializer()

    class Meta:
        model = Karyawan
        fields = '__all__'


class EditRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

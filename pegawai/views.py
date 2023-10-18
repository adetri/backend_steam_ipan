from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fatch_all_pegawai(request):
    if request.method == 'GET':
        pegawai = GetKaryawanSerializer(Karyawan.objects.all(), many=True).data
        data = {"pegawai": pegawai}
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_pegawai(request):
    if request.method == 'POST':
        data = {}
        serializer = KaryawanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new Karyawan record
            data['msg'] = "Success"
            data['pegawai'] = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pegawai(request, pk):
    if request.method == 'GET':
        data = {}
        try:
            qry = Karyawan.objects.get(pk=pk)
            pegawai = GetKaryawanSerializer(qry, many=False).data
            data['pegawai'] = pegawai
            data['msg'] = "Success"
            data['pk'] = "Success"
            specific_field = pegawai.get('field_name', None)
            res_code = status.HTTP_200_OK
        except:
            data['msg'] = "Failed to get data"
            res_code = status.HTTP_204_NO_CONTENT

        return Response(data, status=res_code)
    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_pegawai(request, pk):
    if request.method == 'PUT':
        data = {}
        try:
            qry = Karyawan.objects.get(pk=pk)
        except:
            data['msg'] = "Fail tp get data"
            res_code = status.HTTP_204_NO_CONTENT
            return Response(data, status=res_code)

        serializer = EditkaryawanSerializer(
            qry, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()  # Save the updated data
            data['pegawai'] = serializer.data
            data['msg'] = "Update Success"
            res_code = status.HTTP_202_ACCEPTED
            return Response(data, status=res_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_pegawai(request, pk):
    if request.method == "DELETE":
        data = {}

        try:
            qry = Karyawan.objects.get(pk=pk)
            qry.delete()
            data['msg'] = "Delete data success"
            res_code = status.HTTP_202_ACCEPTED

        except:
            data['msg'] = "Fail tp get data"
            res_code = status.HTTP_204_NO_CONTENT

        return Response(data, status=res_code)

    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fatch_all_role(request):
    if request.method == 'GET':
        role = GetRoleSerializer(Role.objects.all(), many=True).data
        data = {"role": role}
        return Response(data, status=status.HTTP_200_OK)
    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_role(request, pk):
    if request.method == 'GET':
        try:
            role = GetRoleSerializer(Role.objects.get(pk=pk), many=False).data
            data = {"role": role}
            return Response(data, status=status.HTTP_200_OK)
        except:
            return Response("Failed to get data", status=status.HTTP_204_NO_CONTENT)

    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_role(request, pk):
    if request.method == 'PUT':
        data = {}
        try:
            qry = Role.objects.get(pk=pk)
        except:
            data['msg'] = "Fail tp get data"
            res_code = status.HTTP_204_NO_CONTENT
            return Response(data, status=res_code)

        serializer = EditRoleSerializer(
            qry, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()  # Save the updated data
            data['role'] = serializer.data
            data['msg'] = "Update Success"
            res_code = status.HTTP_202_ACCEPTED
            return Response(data, status=res_code)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_role(request, pk):
    if request.method == "DELETE":
        data = {}

        try:
            qry = Role.objects.get(pk=pk)
            qry.delete()
            data['msg'] = "Delete data success"
            res_code = status.HTTP_202_ACCEPTED

        except:
            data['msg'] = "Fail to delete data"
            res_code = status.HTTP_204_NO_CONTENT

        return Response(data, status=res_code)

    else:
        return Response("Method Not Allow", status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_role(request):
    if request.method == 'POST':
        data = {}
        serializer = EditRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new Karyawan record
            data['msg'] = "Success"
            data['pegawai'] = serializer.data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("Method Not Allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)

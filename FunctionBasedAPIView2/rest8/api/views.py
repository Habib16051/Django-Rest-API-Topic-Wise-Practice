from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response


# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request, pk=None):
    if request.method == 'GET':
        # id = request.data.get('id')
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is created'})
        return Response(serializer.errors)

    if request.method == 'PUT':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Updated'})
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is Deleted!'})

    if request.method == 'PATCH':
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is partially Updated'})
        return Response(serializer.errors)



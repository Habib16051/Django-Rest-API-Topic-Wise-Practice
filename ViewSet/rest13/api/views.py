from django.shortcuts import render
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework import viewsets


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        id = pk

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk

        stu = Student.objects.get(id=pk)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        id = pk

        stu = Student.objects.get(id=pk)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is partially Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk

        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is Deleted!!'})


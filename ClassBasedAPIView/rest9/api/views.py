from django.shortcuts import render
from rest_framework import status
# from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
# Class Based APIView
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)

        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is created'})
        return Response(serializer.errors)

    def put(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is partially Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        # id = request.data.get('id')
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg': 'Data is Deleted!'})

from django.shortcuts import render
from .serializers import StudentSerializers
from .models import Student
from rest_framework import viewsets


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

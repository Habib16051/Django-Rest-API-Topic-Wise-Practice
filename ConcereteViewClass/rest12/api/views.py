from .models import Student
from .serializers import StudentSerializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView


# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#
# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# List and Create Combined - Pk is not required

class LCStudent(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


# Retrieve and Update API View Together - PK is required
#
# class RUStudent(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# Retrieve and Destroy API View Together - Pk is required
# class RDStudent(RetrieveDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# Retrieve, Update and Destroy - three all together - pk is required

class RUDStudent(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

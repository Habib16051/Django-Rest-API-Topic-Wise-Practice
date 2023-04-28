from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets


# Create, Retrieve, Update and Destroy all will be work at this time
# class StudentModelViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

# Read Only ViewSet - only List and retrieve operation will be work at this time
class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

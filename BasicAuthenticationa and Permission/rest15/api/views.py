from .models import Student
from .serializers import StudentSerializers
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser


# Create, Retrieve, Update and Destroy all will be work at this time
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]

# # Read Only ViewSet - only List and retrieve operation will be work at this time
# class ReadOnlyStudentModelViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

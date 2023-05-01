# Generic APIView and model mixins
from .models import Student
from .serializers import StudentSerializers
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']

    # def get_queryset(self):
    #     user = self.request.user
    #     return Student.objects.filter(pass_by=user)
    # throttle_classes = [ScopedRateThrottle]
    # throttle_scope = 'viewstu'

# class StudentCreate(CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'createstu'
#
#
# class StudentRetrieve(RetrieveAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'
#
#
# class StudentUpdate(UpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'
#
#
# class StudentDestroy(DestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers
#     throttle_classes = [ScopedRateThrottle]
#     throttle_scope = 'viewstu'

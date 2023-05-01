# Generic APIView and model mixins
from .models import Student
from .serializers import StudentSerializers
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, \
    RetrieveModelMixin
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, RetrieveAPIView, \
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    # filter_backends = [SearchFilter]
    filter_backends = [OrderingFilter]
    # only filter based on name and city
    ordering_fields = ['name', 'city']
    # # search_fields = ['name', 'city']

    # Search Filter [Start With Search]
    # search_fields = ['^name']

    # Search Filter [ For Exact Match]
    # search_fields = ['^name']

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

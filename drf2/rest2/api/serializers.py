from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    # For De-serialization

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

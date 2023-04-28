from rest_framework import serializers
from .models import Student


# Model Serializer Class

class StudentSerializers(serializers.ModelSerializer):
    # Explicitly for model-serializer_validation
    # name = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ['name', 'age', 'city']
        # To valid multiple value in validation rules
        # read_only_fields = ['name', 'age']
        extra_kwargs = {'name': {'read_only': True}}  # We can apply validation rules like this also

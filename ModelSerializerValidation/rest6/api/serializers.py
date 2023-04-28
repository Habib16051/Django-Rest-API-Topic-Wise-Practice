from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):

    # Validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name should be Start with R')

    name = serializers.CharField(validators=[start_with_r])

    class Meta:
        model = Student
        fields = ['name', 'age', 'city']

    # Field Level Validation
    def validate_age(self, value):
        if value >= 50:
            raise serializers.ValidationError('Sorry! You are too old!')
        return value

    # Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'mohi' and ct.lower() != 'barishal':
            raise serializers.ValidationError('City Must be Barishal!!')
        return data

from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name Start with R')


class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):  # Insert /create data into the database (POST method)
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        print(instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

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

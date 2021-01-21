from rest_framework import serializers

from students.models import Student


class StudentDetailSerializer(serializers.ModelSerializer):
    """Serializer of Student model for API processing"""
    class Meta:
        model = Student
        fields = '__all__'

from rest_framework import serializers
from .models import Course, University  # Replace with actual model names

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Specify fields or use '__all__' to include all fields

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'

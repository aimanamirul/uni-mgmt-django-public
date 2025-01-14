from django import forms
from Assignment2.models import University, Course, Admin

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__' #Have the form use all fields in the model Course

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['Username', 'Password', 'Token']


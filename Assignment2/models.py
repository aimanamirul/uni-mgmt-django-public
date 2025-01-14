from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class University(models.Model):
    UniversityID = models.AutoField(primary_key=True)
    UniversityName = models.TextField(null=False,blank=False)
    State = models.TextField()

class Course(models.Model):
    CourseID = models.AutoField(primary_key=True)
    CourseCode = models.TextField(blank =False, null=False)
    CourseTitle = models.TextField(null=False, blank=False)
    ProgramLvl = models.TextField()
    TuitionFees = models.DecimalField(max_digits=8,decimal_places=2)

# 30/11/2024 - Aiman - Included UniversityCourse model as bridge for University -> Course

class UniversityCourse(models.Model):
    #UniversityCourseID = models.AutoField(primary_key=True, default=0)
    Course = models.ForeignKey(Course, to_field='CourseID', on_delete=models.CASCADE)
    University = models.ForeignKey(University, on_delete=models.CASCADE)

class Admin(models.Model):
    AdminID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=255, unique=True)
    Password = models.CharField(max_length=255)
    Token = models.CharField(max_length=255, blank=True, null=True)

    def set_password(self, password):
        self.Password = make_password(password)

    def check_password(self, password):
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.Password)
    
    def __str__(self):
        return self.Username
from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from django.db import DatabaseError, IntegrityError
from Assignment2.models import Course, University, UniversityCourse
from Assignment2.forms import CourseForm, UniversityForm
from django.http import JsonResponse
#Ayman: 1/12/2024
def createUniversity(request): #Create University
    form = UniversityForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            response = {
                'UniversityName': form.save().UniversityName,
            }
            return JsonResponse(response)
    response = {
        'Error': form.errors
    }
    return JsonResponse(response)

def createCourse(request): #Create Course
    form = CourseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            response = {
                'CourseCode': form.save().CourseCode,
                'CourseTitle': form.save().CourseTitle,
            }
            return JsonResponse(response)
        response = {
            'Error': form.errors
        }
    return JsonResponse(response)

def assignCourse(request): #Assign Course to University
    
    if request.method == "POST":
        print("CourseCode",request.POST["CourseCode"])
        print("UniversityID",request.POST["UniversityID"])
        if 'CourseCode' in request.POST and 'UniversityID' in request.POST:
            
            try:
                
                CourseObj = Course.objects.filter(CourseCode = request.POST["CourseCode"]).first()
                UniversityObj = University.objects.filter(UniversityID = request.POST["UniversityID"]).first()
                if CourseObj is None or UniversityObj is None:
                    print("CourseCode and/or UniversityID does not exist")
                    return JsonResponse({'Error':"CourseCode and/or UniversityID does not exist"},safe=False)
                
                UC = UniversityCourse.objects.create(Course = CourseObj, University = UniversityObj)
                print(UC.University.UniversityID)
                response = {
                    'CourseCode': UC.Course.CourseCode,
                    'UniversityID': UC.University.UniversityID
                    }
                return JsonResponse(response, safe=False)
            except Exception as Err:
                return JsonResponse({'Error': str(Err)},safe=False)
        print("CourseCode and/or UniversityID not defined in POST")
        return JsonResponse({'Error': "CourseCode and/or UniversityID not defined in POST"})
    print("Request method is NOT POST")
    return JsonResponse({'Error': "Request method is NOT POST"})
        
        
def obtainCourses(request): #Get Course
    response = list(Course.objects.all().values("CourseCode","CourseTitle"))
    if not response:
        return JsonResponse({'Error':"No Courses right now"},safe=False)
    return JsonResponse(response, safe=False) #Make it accept non Dictionaries

def obtainUniversities(request): #Get Universities
    response = {"Universities":list(University.objects.all().values("UniversityID","UniversityName","State"))}
    if not response:
        return JsonResponse({'Error':"No Universities right now"},safe=False)
    return JsonResponse(response, safe=False) #Make it accept non Dictionaries

def deleteUniversity(request): #Delete University
    if request.method == 'POST':
        if 'UniversityID' in request.POST:
            uni = University.objects.filter(UniversityID = request.POST['UniversityID']).first();
            if uni is None:
                return JsonResponse({'Error':"No Universities right now"},safe=False)
            response = {'UniversityID': uni.UniversityID,
                        'UniversityName':uni.UniversityName
                        };
            try:
                uni.delete();
                return JsonResponse(response,safe=False)
            except Exception as Err:
                return JsonResponse({'Error': str(Err)},safe=False)
    
    return JsonResponse({'Error': 'Unable to delete University'},safe=False)

def deleteCourse(request):
    if request.method == 'POST':
        if 'CourseCode' in request.POST:
            course = Course.objects.filter(CourseCode = request.POST['CourseCode']).first();
            if course is None:
                return JsonResponse({'Error':"No Courses right now"},safe=False)
            response = {'CourseCode': course.CourseCode,
                        'CourseTitle': course.CourseTitle
                        };
            try:
                course.delete();
                return JsonResponse(response,safe=False)
            except Exception as Err:
                return JsonResponse({'Error': str(Err)},safe=False)
    
    return JsonResponse({'Error': 'Unable to delete Course'},safe=False)

def deleteAssignment(request):
    if request.method == 'POST':
        if 'CourseCode' in request.POST and 'UniversityID' in request.POST:
            course = Course.objects.filter(CourseCode = request.POST['CourseCode']).first();
            uni = University.objects.filter(UniversityID = request.POST['UniversityID']).first();
            
            if course is None or course is None:
                return JsonResponse({'Error':"No Courses or Universities right now"},safe=False)
            uniCourse = UniversityCourse.objects.filter(University = uni, Course = course).first();
            if uniCourse is None:
                return JsonResponse({'Error':"No Course in University"},safe=False)
            response = {'CourseCode': course.CourseCode,
                        'UniversityID':uni.UniversityID
                        };
            try:
                uniCourse.delete()
                return JsonResponse(response,safe=False)
            except Exception as Err:
                return JsonResponse({'Error': str(Err)},safe=False)
    
    return JsonResponse({'Error': 'Unable to delete Course'},safe=False)

def obtainUniversities_and_FirstUniFirstCourse(request):
    Uni = University.objects.all()
    if not Uni.exists():
        JsonResponse({"Error":"University list is empty!"},safe=False)
    FirstCourseAssignment = UniversityCourse.objects.filter(University = Uni.first()).first()
    if FirstCourseAssignment is None:
        response = {"Universities":list(University.objects.all().values("UniversityID","UniversityName","State"))}
    else:
        response = {"Universities":list(University.objects.all().values("UniversityID","UniversityName","State")),
                    "CourseCode": FirstCourseAssignment.Course.CourseCode
                    }
    return JsonResponse(response, safe=False) #Make it accept non Dictionaries
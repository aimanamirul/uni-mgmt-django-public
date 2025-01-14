from django.http import JsonResponse, HttpResponse
from Assignment2.models import UniversityCourse, Course
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import CourseSerializer

def get_courses_by_university(request, university_id):
    if request.method == 'GET':
        courses = UniversityCourse.objects.filter(University_id=university_id).select_related('Course')
        course_list = [
            {
                'CourseID': course.Course.CourseID,
                'CourseCode': course.Course.CourseCode,
                'CourseTitle': course.Course.CourseTitle,
                'ProgramLvl': course.Course.ProgramLvl,
                'TuitionFees': course.Course.TuitionFees,
            } 
            for course in courses
        ]
        return JsonResponse(course_list, safe=False)

def get_all_courses(request): #Get Course
    if request.method == 'GET':
        response = list(Course.objects.all().values())
        if not response:
            return HttpResponse("No Courses right now")
        return JsonResponse(response, safe=False) #Make it accept non Dictionaries

@api_view(['PUT'])
def update_course(request, id):
    try:
        course = Course.objects.get(pk=id)
    except Course.DoesNotExist:
        return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CourseSerializer(course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_courses_by_university(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        university_id = data.get('university_id')
        course_ids = data.get('course_ids', [])
        UniversityCourse.objects.filter(University_id=university_id, Course_id__in=course_ids).delete()
        return JsonResponse({'message': 'Courses deleted successfully'}, status=200)

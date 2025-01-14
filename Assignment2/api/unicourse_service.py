from django.http import JsonResponse
from Assignment2.models import UniversityCourse, Course

def get_courses_by_university(request, university_id):
    if request.method == 'GET':
        courses = UniversityCourse.objects.filter(University_id=university_id).select_related('Course')
        course_list = [
            {
                'CourseCode': course.Course.CourseCode,
                'CourseTitle': course.Course.CourseTitle,
                'ProgramLvl': course.Course.ProgramLvl,
                'TuitionFees': course.Course.TuitionFees,
            } 
            for course in courses
        ]
        return JsonResponse(course_list, safe=False)

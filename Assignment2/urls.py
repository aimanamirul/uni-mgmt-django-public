from django.urls import path
from . import views
from . import queries
from .api.university_service import create_university, update_university, view_university, delete_university, list_universities
from .api.course_service import get_courses_by_university, get_all_courses, update_course, delete_courses_by_university

urlpatterns = [
    path("",views.admin_login,name='create_login'),
    path('register/', views.create_admin_account, name='create_admin'),
    path('logout/', views.logout_view, name='logout'),    
    # path('login/', views.admin_login, name='admin_login'),

    path("create/", views.createInterface,name = "CreateInterface"),
    path("view/", views.viewInterface, name="ViewInterface"),
    # path("edit/", views.editInterface, name="EditInterface"),
    path('edit/<str:mode>/<int:id>/', views.editInterface, name='EditInterface'),
    path("delete/", views.deleteInterface, name="DeleteInterface"),

    path('query/universities/', create_university, name='create_university'),
    path('query/universities/<int:id>/', view_university, name='view_university'),
    path('query/universities/<int:id>/update/', update_university, name='update_university'),
    path('query/universities/<int:id>/delete/', delete_university, name='delete_university'),
    path('query/universities/get/', list_universities, name='list_universities'),
    path('query/courses/get/', get_all_courses, name='get_all_courses'),
    path('query/universitycourse/get/<int:university_id>/', get_courses_by_university, name='get_courses_by_university'),
    path('query/courses/<int:id>/update/', update_course, name='update_course'),
    path('query/universitycourse/delete/', delete_courses_by_university, name='delete_courses_by_university'),

    #Ayman: 1/12/2024
    path("query/createUniversity/",queries.createUniversity, name="CreateUniversity"),
    path("query/createCourse/",queries.createCourse, name="CreateCourse"),
    path("query/assignCourse/",queries.assignCourse,name="AssignCourse"),
    path("query/obtainCourses/",queries.obtainCourses,name="ObtainCourses"),
    path("query/obtainUniversities/",queries.obtainUniversities,name="ObtainUniversities"),
    path("query/deleteUniversity/",queries.deleteUniversity,name="DeleteUniversity"),
    path("query/deleteCourse/",queries.deleteCourse,name="DeleteCourse"),
    path("query/deleteCourseAssignedToUniversity/",queries.deleteAssignment,name="deleteCourseAssignedToUniversity"),
    path("query/obtainUniversities_and_FirstUniFirstCourse/",queries.obtainUniversities_and_FirstUniFirstCourse,name="obtainUniversities_and_FirstUniFirstCourse"),
]
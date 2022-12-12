"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student import views as student_views
from teacher import views as teacher_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/group/', student_views.StudentClassAPIViewSet.as_view({
        'post': 'create', 'get': 'list'
    })),
    # path('api/group/<int:pk>/', student_views.StudentAPIViewSet.as_view({
    #     'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    # })),
    path('api/student/', student_views.StudentListAPIViewSet.as_view({
        'get': 'list'
    })),
    path('api/student/<int:pk>/', student_views.StudentDetailAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/student/addstudent/', student_views.AddStudentAPIViewSet.as_view({
        'post': 'create'
    })),
    path('api/teacher/', teacher_views.TeacherListAPIViewSet.as_view({
        'get': 'list'
    })),
    path('api/teacher/<int:pk>/', teacher_views.TeacherDetailAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/teacher/addteacher/', teacher_views.AddTeacherAPIViewSet.as_view({
        'post': 'create'
    })),
    path('api/notification/', teacher_views.NotificationAPIViewSet.as_view({
        'post': 'create', 'get': 'list'
    })),
    path('api/notification/<int:pk>/', teacher_views.NotificationAPIViewSet.as_view({
        'get': 'retrieve', 'delete': 'destroy'
    })),
    path('api/attendance/', student_views.AttendanceAPIViewSet.as_view({
        'post': 'create', 'get': 'list'
    })),
    path('api/attendance/<int:pk>/', student_views.AttendanceAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/subject/', teacher_views.TeacherSubjectInfoAPIViewSet.as_view({
        'get': 'list'
    })),
    path('api/subject/group/', student_views.StudentSubjectClassAPIViewSet.as_view({
        'get': 'list'
    })),
    path('api/subject/group/<int:pk>/', student_views.StudentSubjectClassAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('api/rate/', student_views.RateAPIViewSet.as_view({
        'post': 'create', 'get': 'list'
    })),
    path('api/rate/<int:pk>/', student_views.RateAPIViewSet.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
]
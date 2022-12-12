from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class StudentClassAPIViewSet(ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentClassSerializer
    pagination_class = PageNumberPagination


class StudentSubjectClassAPIViewSet(ModelViewSet):
    queryset = StudentClass.objects.all()
    serializer_class = StudentSubjectClassSerializer
    pagination_class = PageNumberPagination




class StudentListAPIViewSet(ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentListSerializer
    pagination_class = PageNumberPagination


class StudentDetailAPIViewSet(ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentDetailSerializer
    pagination_class = PageNumberPagination


class AddStudentAPIViewSet(ModelViewSet):
    queryset = StudentInfo.objects.all()
    serializer_class = StudentDetailSerializer
    pagination_class = PageNumberPagination


class AttendanceAPIViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    pagination_class = PageNumberPagination


class RateAPIViewSet(ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    pagination_class = PageNumberPagination
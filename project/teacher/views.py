from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination



class TeacherListAPIViewSet(ModelViewSet):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherListSerializer
    pagination_class = PageNumberPagination


class TeacherDetailAPIViewSet(ModelViewSet):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherDetailSerializer
    pagination_class = PageNumberPagination


class AddTeacherAPIViewSet(ModelViewSet):
    queryset = TeacherInfo.objects.all()
    serializer_class = TeacherDetailSerializer
    pagination_class = PageNumberPagination


class NotificationAPIViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = PageNumberPagination


class TeacherSubjectInfoAPIViewSet(ModelViewSet):
    queryset = TeacherSubjectInfo.objects.all()
    serializer_class = TeacherSubjectInfoSerializer
    pagination_class = PageNumberPagination
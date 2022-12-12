from .models import *
from rest_framework import serializers


class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ["id", "group"]


class StudentSubjectClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    group = serializers.ReadOnlyField(source='group.group')
    class Meta:
        model = StudentInfo
        fields = ('id name email admission_id group').split()


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    subject = serializers.ReadOnlyField(source='subject.subject')
    class Meta:
        model = Attendance
        fields = "__all__"


class RateSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    subject = serializers.ReadOnlyField(source='subject.subject')
    class Meta:
        model = Rate
        fields = "__all__"
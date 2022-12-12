from django.db import models
from teacher.models import *


class StudentClass(models.Model):
    group = models.CharField(max_length=20)
    curator = models.ForeignKey(TeacherInfo, on_delete=models.CASCADE, null=True)
    subject = models.ManyToManyField(TeacherSubjectInfo)

    def __str__(self):
        return self.group


class StudentInfo(models.Model):
    academic_year = models.CharField(max_length=100)
    admission_date = models.DateField()
    admission_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    number = models.IntegerField(unique=True, null=True)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    group = models.ForeignKey(StudentClass, on_delete=models.CASCADE, null=True)
    student_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    parents_name = models.CharField(max_length=100)
    parent_number = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    status = (
        ('absent', 'Absent'),
        ('present', 'Present'),
        ('laneness', 'Lateness'),
        ('5 min late', '5 min late'),
        ('10 min late', '10 min late'),
        ('15 min late', '15 min late'),
        ('20 min late', '20 min late'),
    )

    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    subject = models.ForeignKey(TeacherSubjectInfo, on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=status, max_length=100)

    def __str__(self):
        return self.student.admission_id



class Rate(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    subject = models.ForeignKey(TeacherSubjectInfo, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return self.student.name





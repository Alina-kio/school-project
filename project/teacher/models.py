from django.db import models



class TeacherSubjectInfo(models.Model):
    subject = models.CharField(max_length=50)
    # time = models.TimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.subject

class TeacherInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    teacher_img = models.ImageField()
    joining_date = models.DateField()
    subject = models.ForeignKey(TeacherSubjectInfo, on_delete=models.CASCADE, null=True)
    # subject = models.ManyToManyField(TeacherSubjectInfo)
    salary = models.IntegerField()

    def __str__(self):
        return self.name



class Notification(models.Model):
    techer = models.ForeignKey(TeacherInfo, on_delete=models.DO_NOTHING)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField()
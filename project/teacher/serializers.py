from .models import *
from rest_framework import serializers
# from rest_framework.exceptions import ValidationError

# def teacher_list(request):
#     teachers = TeacherInfo.objects.all()

#     paginator = Paginator(teachers, 1)
#     page = request.GET.get('page')
#     paged_teachers = paginator.get_page(page)
#     context = {
#         "teachers": paged_teachers
#     }
#     return render(request, "teachers/teacher_list.html", context)


# def single_teacher(request, teacher_id):
#     single_teacher = get_object_or_404(TeacherInfo, pk=teacher_id)
#     context = {
#         "single_teacher": single_teacher
#     }
#     return render(request, "teachers/single_teacher.html", context)


# def create_teacher(request):
#     if request.method == "POST":
#         forms = CreateTeacher(request.POST, request.FILES or None)

#         if forms.is_valid():
#             forms.save()
#         messages.success(request, "Teacher Registration Successfully!")
#         return redirect("teacher_list")
#     else:
#         forms = CreateTeacher()

#     context = {
#         "forms": forms
#     }
#     return render(request, "teachers/create_teacher.html", context)


# def edit_teacher(request, pk):
#     teacher_edit = TeacherInfo.objects.get(id=pk)
#     edit_teacher_forms = CreateTeacher(instance=teacher_edit)

#     if request.method == "POST":
#         edit_teacher_forms = CreateTeacher(request.POST, request.FILES or None, instance=teacher_edit)

#         if edit_teacher_forms.is_valid():
#             edit_teacher_forms.save()
#             messages.success(request, "Edit Teacher Info Successfully!")
#             return redirect("teacher_list")

#     context = {
#         "edit_teacher_forms": edit_teacher_forms
#     }
#     return render(request, "teachers/edit_teacher.html", context)


# def delete_teacher(request, teacher_id):
#     teacher_delete = TeacherInfo.objects.get(id=teacher_id)
#     teacher_delete.delete()
#     messages.success(request, "Delete Teacher Info Successfully")
#     return redirect("teacher_list")




class TeacherListSerializer(serializers.ModelSerializer):
    subject = serializers.ReadOnlyField(source='subject.subject')
    class Meta:
        model = TeacherInfo
        fields = ('id name email subject').split()


class TeacherDetailSerializer(serializers.ModelSerializer):
    subject = serializers.ReadOnlyField(source='subject.subject')
    class Meta:
        model = TeacherInfo
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"


class TeacherSubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherSubjectInfo
        fields = "__all__"

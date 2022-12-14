# Generated by Django 4.1.4 on 2022-12-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_attendance_date'),
        ('teacher', '0003_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachersubjectinfo',
            old_name='sub_name',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='teachersubjectinfo',
            name='student',
            field=models.ManyToManyField(to='student.studentinfo'),
        ),
    ]

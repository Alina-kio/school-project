# Generated by Django 4.1.4 on 2022-12-10 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_remove_teachersubjectinfo_student'),
        ('student', '0011_remove_studentclassname_student_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentSubject',
            new_name='StudentClass',
        ),
        migrations.DeleteModel(
            name='StudentClassName',
        ),
    ]

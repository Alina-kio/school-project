# Generated by Django 4.1.4 on 2022-12-09 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_remove_teachersubjectinfo_student'),
        ('student', '0007_rename_class_name_studentclass_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teachersubjectinfo')),
            ],
        ),
    ]

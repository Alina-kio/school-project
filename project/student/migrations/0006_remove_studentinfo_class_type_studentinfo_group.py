# Generated by Django 4.1.4 on 2022-12-09 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_alter_attendance_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='class_type',
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentclass'),
        ),
    ]

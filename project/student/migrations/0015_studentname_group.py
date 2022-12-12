# Generated by Django 4.1.4 on 2022-12-10 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0014_alter_attendance_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studentinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=20)),
                ('student', models.ManyToManyField(to='student.studentname')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-09 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacherinfo_teacher_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('date', models.DateTimeField()),
                ('techer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teacher.teacherinfo')),
            ],
        ),
    ]

# Generated by Django 4.1.4 on 2022-12-09 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='teacher_img',
            field=models.ImageField(upload_to=''),
        ),
    ]

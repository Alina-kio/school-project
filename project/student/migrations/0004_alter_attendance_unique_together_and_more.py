# Generated by Django 4.1.4 on 2022-12-09 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_attendance'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now_add=True, unique=True),
        ),
    ]

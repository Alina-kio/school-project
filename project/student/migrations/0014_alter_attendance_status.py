# Generated by Django 4.1.4 on 2022-12-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_attendance_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('absent', 'Absent'), ('present', 'Present'), ('laneness', 'Lateness'), ('5 min late', '5 min late'), ('10 min late', '10 min late'), ('15 min late', '15 min late'), ('20 min late', '20 min late')], max_length=100),
        ),
    ]
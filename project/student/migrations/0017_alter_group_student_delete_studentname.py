# Generated by Django 4.1.4 on 2022-12-10 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_alter_group_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='student',
            field=models.ManyToManyField(related_name='student_name', to='student.studentinfo'),
        ),
        migrations.DeleteModel(
            name='StudentName',
        ),
    ]
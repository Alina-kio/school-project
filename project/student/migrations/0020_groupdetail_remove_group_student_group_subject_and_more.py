# Generated by Django 4.1.4 on 2022-12-10 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_remove_teachersubjectinfo_student'),
        ('student', '0019_alter_group_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ManyToManyField(to='teacher.teachersubjectinfo'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.group'),
        ),
        migrations.DeleteModel(
            name='StudentClass',
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group1', to='student.group'),
        ),
        migrations.AddField(
            model_name='groupdetail',
            name='student',
            field=models.ManyToManyField(related_name='student_name', to='student.studentinfo'),
        ),
    ]

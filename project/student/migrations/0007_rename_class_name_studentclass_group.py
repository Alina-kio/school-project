# Generated by Django 4.1.4 on 2022-12-09 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_remove_studentinfo_class_type_studentinfo_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentclass',
            old_name='class_name',
            new_name='group',
        ),
    ]
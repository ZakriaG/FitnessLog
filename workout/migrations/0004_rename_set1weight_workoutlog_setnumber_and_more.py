# Generated by Django 4.2.2 on 2023-08-15 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0003_rename_name_workoutlog_exercisename_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workoutlog',
            old_name='Set1Weight',
            new_name='SetNumber',
        ),
        migrations.RenameField(
            model_name='workoutlog',
            old_name='Set2Weight',
            new_name='Weight',
        ),
        migrations.RemoveField(
            model_name='workoutlog',
            name='Set3Weight',
        ),
        migrations.RemoveField(
            model_name='workoutlog',
            name='Set4Weight',
        ),
    ]

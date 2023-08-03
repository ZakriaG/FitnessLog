# Generated by Django 4.2.2 on 2023-08-03 18:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workoutlog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

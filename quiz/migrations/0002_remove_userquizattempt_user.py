# Generated by Django 5.0.6 on 2024-07-03 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userquizattempt',
            name='user',
        ),
    ]

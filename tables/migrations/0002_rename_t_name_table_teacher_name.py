# Generated by Django 5.0.6 on 2024-07-28 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='t_name',
            new_name='teacher_name',
        ),
    ]

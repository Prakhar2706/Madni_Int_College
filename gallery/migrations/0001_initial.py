# Generated by Django 5.0.6 on 2024-07-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gallery_img', models.FileField(blank=True, default='', null=True, upload_to='gallery/')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-13 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]

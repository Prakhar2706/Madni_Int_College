# Generated by Django 5.0.6 on 2024-07-14 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_announcement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Floating_img', models.FileField(blank=True, default='', max_length=250, null=True, upload_to='floating/')),
            ],
        ),
    ]
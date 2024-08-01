from django.db import models

# Create your models here.
class About(models.Model):
    about=models.TextField(max_length=2000, default="")

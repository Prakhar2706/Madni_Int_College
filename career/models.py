from django.db import models

# Create your models here.
class Career(models.Model):
    career_heading=models.CharField(max_length=100,default="")
    career_des=models.TextField(default="")
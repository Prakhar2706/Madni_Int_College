from django.db import models

# Create your models here.
class Table(models.Model):
    day=models.CharField(max_length=15,default="")
    period_1=models.CharField(max_length=100,default="")
    period_2=models.CharField(max_length=100,default="")
    period_3=models.CharField(max_length=100,default="")
    period_4=models.CharField(max_length=100,default="")
    period_5=models.CharField(max_length=100,default="")
    period_6=models.CharField(max_length=100,default="")
    period_7=models.CharField(max_length=100,default="")
    period_8=models.CharField(max_length=100,default="")
    
  
    
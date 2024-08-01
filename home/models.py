from django.db import models

# Create your models here.
class Event(models.Model):
    Event_date=models.CharField(max_length=20,default="")
    Event_month=models.CharField(max_length=20,default="")
    Event_des=models.CharField(max_length=50,default="")

class News(models.Model):
    News_name=models.CharField(max_length=20,default="")
    News_des=models.CharField(max_length=120,default="")
    
class Announcement(models.Model):
    Announcement_name=models.CharField(max_length=200,default="")
    Announcement_des=models.CharField(max_length=100,default="")
class Floating(models.Model):
    Floating_img=models.FileField(upload_to="floating/",max_length=250,default="",blank=True,null=True)        


    
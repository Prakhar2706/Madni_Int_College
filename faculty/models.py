from django.db import models

# Create your models here.
class Faculty(models.Model):
    Faculty_name=models.CharField(max_length=30,default="")
    Faculty_degree=models.CharField(max_length=30,default="")
    Faculty_address=models.CharField(max_length=100,default="")
    Faculty_contact=models.CharField(max_length=50,default="")
    Faculty_email=models.CharField(max_length=50,default="")
    Faculty_img=models.FileField(upload_to="faculty/", max_length=120, default="",blank=True,null=True)

def __str__(self):
    return self.name

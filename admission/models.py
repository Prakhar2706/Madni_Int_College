from django.db import models

# Create your models here.
class Admission_Form(models.Model):
    Full_Name=models.CharField(max_length=50, default="")
    Father_Name=models.CharField(max_length=50,default="")
    Mother_Name=models.CharField(max_length=50,default="")
    Email=models.EmailField(max_length=40,default="")
    Contact=models.CharField(max_length=20,default="")
    Whatsapp_Contact=models.CharField(max_length=20,default="")
    Address=models.CharField(max_length=150,default="")
    Date_of_Birth=models.CharField(max_length=20,default="")
    Gender=models.CharField(max_length=15,default="")
    Class=models.CharField(max_length=20,default="")
    

def __str__(self):
    return self.name
    
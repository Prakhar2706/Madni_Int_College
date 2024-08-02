from django.db import models

# Create your models here.
class Gallery(models.Model):
    Gallery_img = models.FileField(upload_to="gallery/", max_length=100, default="", blank=True, null=True)

def __str__(self):
    return self.name

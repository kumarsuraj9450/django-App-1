from django.db import models

# Create your models here.
class image_file(models.Model):
    image  = models.ImageField(upload_to='uploaded_pic',blank=False,null=True)
    url    = models.URLField(blank=True,null=True,default='')

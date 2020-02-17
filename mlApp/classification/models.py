from django.db import models

# Create your models here.
class dimensions(models.Model):
    petalWidth  =models.DecimalField(decimal_places=2,max_digits=4,blank=False,null=False)
    petalLength =models.DecimalField(decimal_places=2,max_digits=4,blank=False,null=False)
    sepalWidth  =models.DecimalField(decimal_places=2,max_digits=4,blank=False,null=False)
    sepalLength =models.DecimalField(decimal_places=2,max_digits=4,blank=False,null=False)
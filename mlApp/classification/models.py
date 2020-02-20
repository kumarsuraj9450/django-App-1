from django.db import models

# from fastai.vision import *

# Create your models here.
class image_file(models.Model):
    image  = models.ImageField(upload_to='uploaded_pic',blank=False,null=True)
    url    = models.URLField(blank=True,null=True,default='')

    def predict(self):
        # learner = load_learner('.','stage-1-export-file.pkl')
        # predictedClass = learner.predict(self.image.url)
        pass
        predictedClass = 'Class'
        return predictedClass

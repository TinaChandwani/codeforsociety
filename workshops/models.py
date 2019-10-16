from django.db import models
from datetime import datetime
from facilitators.models import Facilitator
# Create your models here. defined by class
class Workshop(models.Model):
    facilitator = models.ForeignKey(Facilitator, on_delete=models.DO_NOTHING,default="Anonymous")
    title = models.CharField(max_length= 200)
    venue = models.CharField(max_length= 200)
    city  = models.CharField(max_length= 100)
    description = models.TextField(blank= True)
    price = models.IntegerField()
    team = models.IntegerField(default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    is_published =models.BooleanField(default=True)
    workshop_date = models.DateTimeField(default= datetime.now, blank= True)
    # pick a main field to be displayed

    def __str__(self):
        return self.title


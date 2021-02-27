from django.db import models
from datetime import datetime
# Create your models here.

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/' , blank=True)
    description = models.TextField(blank=True )
    email = models.CharField(max_length=50 ,blank=True)
    phone=  models.CharField(max_length=20 ,blank=True)
    is_seller_of_month = models.BooleanField(default=False , blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    # aaa = models.TextField(default='')

    def __str__(self):
        return self.name


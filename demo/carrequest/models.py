from django.db import models

# Create your models here.

class Carrequest(models.Model):
    take_car_name = models.CharField(max_length=33 , blank=True , null=True)
    take_realtor = models.CharField(max_length=20, blank=True , null=True)
    take_customer = models.CharField(max_length=20, blank=True , null=True)
    take_message = models.TextField( blank=True , null=True)
    

    def __str__(self):
        return self.take_car_name




       
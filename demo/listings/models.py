from django.db import models
from datetime import datetime
from realtors.models import Realtor  # Realtor is the name of the class inside the realtors model 
from brand.models import Brand
from accounts.models import Accounts
# Create your models here.
uu = [('','')]
class Listing(models.Model): # model name 
    realtor  = models.ForeignKey(Realtor,on_delete=models.DO_NOTHING) # this is a foreign key from Realtor model ,,the scond parameter to define what will happens if i delete the realtor that is attached to listing 
    car_brand = models.ForeignKey(Brand , on_delete=models.CASCADE)
    car_user = models.ForeignKey(Accounts , on_delete=models.DO_NOTHING , null=True , blank=True)
    
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    description = models.TextField(blank = True) # means that the desc is optional 
    price = models.IntegerField()
    is_published = models.BooleanField(default=True)
    NO_seats = models.IntegerField()
    # the list_date by default will take the current date
    lsit_date = models.DateTimeField(default=datetime.now,blank=True)
#anything i upload like images or files will go to the media folder and from the media folder will be uploaded to the website
# now we wnat to define the folder we want inside that mdeia folder 
# we name the folder inside the media --> photos
# i want to each pic goes in certain structure in the media as -->>> year-month-day
# and i want each pic should be optional --> blank = True 
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


# i want a main field to be diplayed --> we should use title 
# --> __str__ ---->>>> print(str(obj))
    def __str__(self):
        return self.title



class Testing(models.Model):
    name = models.CharField(max_length=22)



    def __str__(self):
        return self.name
        
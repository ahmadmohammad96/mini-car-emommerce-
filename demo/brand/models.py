from django.db import models

# Create your models here.
class Brand(models.Model):
    br_name = models.CharField(max_length=20)
    br_cars_inside_company = models.IntegerField()
    br_description = models.TextField(blank=True , null= True)



    def __str__(self):
        return self.br_name
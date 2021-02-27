from django.contrib import admin

# Register your models here.
from .models import Brand
class BrandAdmin(admin.ModelAdmin):
    list_display = ('br_name' , 'br_cars_inside_company' )

admin.site.register(Brand , BrandAdmin)

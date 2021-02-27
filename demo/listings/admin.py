from django.contrib import admin
from .models import Listing , Testing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
#     # this class will allow me to add extra info in the listings in admin area
    list_display = ('id','title','is_published','price','address','city','lsit_date','realtor')


admin.site.register(Listing , ListingAdmin)
admin.site.register(Testing)
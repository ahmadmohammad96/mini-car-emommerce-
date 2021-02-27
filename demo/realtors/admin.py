from django.contrib import admin
from .models import Realtor
# Register your models here.


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','hire_date','is_seller_of_month')
    list_display_links = ('id','name')
    list_per_page = 5
    list_editable = ('is_seller_of_month',)
    list_filter = ('name',)
    search_fields = ('name',)
admin.site.register(Realtor,RealtorAdmin)
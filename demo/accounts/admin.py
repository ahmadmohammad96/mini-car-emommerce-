from django.contrib import admin

# Register your models here.
from .models import Accounts
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    # this class will allow me to add extra info in the listings in admin area
    list_display = ('id','email','username','last_login','admin','staff','customer','first_name')
    list_display_links = ('id','username') # when i click on id or title will take me to the info
    # list_filter = ('realtor','title')
    list_editable = ('staff','customer')
    # search_fields = ('title','city','address')
    list_per_page = 4

admin.site.register(Accounts,AccountAdmin)
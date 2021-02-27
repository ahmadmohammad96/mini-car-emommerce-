from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

ll = Listing.objects.order_by('-lsit_date').filter(is_published=True)[:3] # 3 means only 3 results 
new_l2 = Listing.objects.all()
con = {'ll_key' : ll, 'new_l2' : new_l2}


rel_l = Realtor.objects.order_by('-hire_date')
s_o_m = Realtor.objects.all().filter(is_seller_of_month=True)
new_d = {'rel_ll' : rel_l , 'som': s_o_m }
# the method usally used for render a template for home page as ex 
# so we import the render method 
# render takes 2 params --> 1 for the request it self && 2 for the location of the template
def index(request):
    return render(request,'pages/index.html' , con)

def about(request):
    return render(request,'pages/about.html',new_d)


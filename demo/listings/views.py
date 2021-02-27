from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Listing
from realtors.models import Realtor
from .choices import *
from accounts.models import Accounts
from .uniq import *
from django.contrib.auth.models import User

from carrequest.models import Carrequest

def index(request):
    # listing is the name of the model ( class )  inside the listing -> models.py
    # asss = Realtor.objects.all().get(name='Jenny Johnson')
    listi = Listing.objects.order_by('-lsit_date').filter(is_published=True) # the earlist will be the firt , 
    
    # NOTICE : the dicti CAN have 2 parameters --> 2 keys
    context = {'lis' : listi  }
    # asss.aaa +='aaaaaaaaaaaaaaaaaaa'
    # asss.save()
    # print(asss.aaa)
    # we can add a second parameter to the render --> a dict
    # like {'name' : 'ahmad '}
    # and in the html page --> listings.html
    return render(request, 'listings/listings.html',context)

def listing(request,listing_id):
    li = get_object_or_404(Listing,pk=listing_id)
    # test = Listing.objects.get(id=5)
    # li2 = Realtor.objects.all()
    contex = {'li' : li }
    t_car = ''
    t_customer = ''
    t_realtor = ''
    t_message = ''
    idd = ''
    if request.method == 'POST':
        print('making the inqury')
        try:

            print('@@@@@@@@@@@@@@')
            print(li.realtor)
            print(listing_id)
            idd = listing_id
            # print(Listing.objects.all().filter(id=2))
            t_car = Listing.objects.all().get(id=idd)
            t_customer = Accounts.objects.all().get(username=request.POST['uname'])
            print(t_customer)
            t_realtor =  Realtor.objects.all().get(name=li.realtor)
            print(t_realtor)
            t_message = request.POST['message']
            print(t_car , t_customer , t_realtor , t_message)
            print('--------')
            # a = Carrequest(take_car_name='aa' , take_customer='bb' , take_realtor ='cc'  , take_message ='dd'  )
            # a.save()
            new_car_request_object = Carrequest()
            print('11')
            new_car_request_object.take_car_name = t_car
            print( 't_car')
            new_car_request_object.take_customer = t_customer
            new_car_request_object.take_realtor = t_realtor
            new_car_request_object.take_message = t_message
            print(new_car_request_object.take_car_name  ,new_car_request_object.take_customer , new_car_request_object.take_realtor , new_car_request_object.take_message )

            new_car_request_object.save()
        except:
            pass

    return render( request,'listings/listing.html',contex)

def search(request):
    new_qu = Listing.objects.all()

    que_list = Listing.objects.order_by('-lsit_date')

    if 'kwords' in request.GET:
        take_keyword = request.GET.get('kwords')
        if take_keyword:
            que_list = que_list.filter(description__icontains=take_keyword)

    if 'city' in request.GET:
        take_city = request.GET['city']
        if take_city:
            que_list = que_list.filter(city__iexact=take_city)
    
    if 'address' in request.GET:
        take_address = request.GET['address']
        if take_address:
            que_list =que_list.filter(address__iexact=take_address)

    if 'Num_seats' in request.GET:
        take_Num_seats = request.GET['Num_seats']
        if take_Num_seats:
            que_list =que_list.filter(NO_seats__iexact=take_Num_seats)    

    if 'price' in request.GET:
        take_price = request.GET['price']
        if take_price:
            que_list = que_list.filter(price__lte=take_price) # lte less_than_or_equal --> at most the price
            
    new_cont = {'num_seats' : num_seats , 'prices' : prices , 'cities' : cities , 'que_list' : que_list ,
     'values' : request.GET , 'new_qu' : new_qu} 
    return render( request,'listings/search.html',new_cont)
    





def updatecar(request , listing_id):

    act_car= ''
    try:
        act_car = get_object_or_404(request , id=listing_id)



    except:
        pass

    



    return render(request , 'index.html' , {})
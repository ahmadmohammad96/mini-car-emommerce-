from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from listings.models import Listing
from accounts.models import Accounts
from apiCar.serializers import CarSerializer



@api_view(['GET' , ])
def apiview(request , id_car):
    print(id_car)
    act_car = ''
    try:  
        act_car = Listing.objects.all().get(id=id_car)
        print(act_car)

    except:
        print('..............')
        return Response(status=status.HTTP_404_NOT_FOUND)

    
    serializer = CarSerializer(act_car)
    print(dir(serializer))
    print(serializer.get_fields)
    
    set_fields = serializer.fields
    list_fields = serializer.get_fields
    for i in list_fields():
        print(i)
    print(type(serializer.data))
    for i in serializer.data.keys():
        print(i)
    # return render(request , 'api1.html' , {'sa' : serializer.data})

    return Response(serializer.data['title'])



# very important to update just a single fields inside a car object 0_0
@api_view(['PUT'])
def api_update_view(request , id_car):

    act_car = ''
    try:
        act_car = Listing.objects.all().get(id=id_car)

    except:
        pass

    take1 = {}
    take2 = {}
    take2 = request.data

    ser = CarSerializer(act_car)
    # for i in ser.data.items():
        # take1.update({i})
    take1 = ser.data
    take1.update(take2)
    # print('...' , take1)
    # print(dir(request.data))
    serializer = CarSerializer(act_car , data=take1)
    cont = {}
    if serializer.is_valid():
        serializer.save()
        cont['success']  = 'updates OK'
        return Response(data=cont)

    return Response( status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def api_delete_view(request , id_car):

    act_car = ''
    try:
        act_car = Listing.objects.all().get(id=id_car)

    except:
        pass
    cont = {}
    if request.method == 'DELETE':
        if act_car.delete():
            cont['success'] = 'deleted'
        else:
            cont['faild'] = 'shit'

        return Response(data=cont)



@api_view(['POST' ,'GET'])
def api_post_view(request):
    print('...............')
    take = request.session['username']
    print(take)
    
    return Response(status=status.HTTP_200_OK)
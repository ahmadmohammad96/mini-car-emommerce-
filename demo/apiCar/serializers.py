from rest_framework import serializers

from listings.models import Listing

 
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = Listing
        fields = ['title' , 'address' , 'city' , 'price']
    



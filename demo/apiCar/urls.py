from django.http import request
from django.urls import path
from . import views

app_name = 'apiCar'
urlpatterns = [
    path('<int:id_car>/' ,views.apiview , name='apiview'),
    path('<int:id_car>/update' , views.api_update_view , name='api_update_view'),  
    path('<int:id_car>/delete' , views.api_delete_view , name='api_delete_view') , 
    path('post_car_api/' , views.api_post_view , name='api_post_view' ),
]
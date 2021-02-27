from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index,name='listings'),
    path('<int:listing_id>',views.listing,name='listing'),# in chrome url --> localhost:8080/listings/21 as ex
    path('search',views.search,name='search'),
    path('<int:listing_id>/update' , views.updatecar , name='updatecar'),
]  
from django import urls
from django.urls import path
from . import views
# from views import brand

urlpatterns = [
    path('' , views.brand , name='brand')
]
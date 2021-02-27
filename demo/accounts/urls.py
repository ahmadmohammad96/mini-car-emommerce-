from django.urls import path 
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),# in chrome url --> localhost:8080/listings/21 as ex
    path('logout',views.logout,name='logout'),
    path('dashboard',views.dashboard,name='dashboard'),

]  
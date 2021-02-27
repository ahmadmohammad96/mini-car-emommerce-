from django.urls import path
from . import views

# the first parametr is empty -->  i mean the home page ( the root page )
# --->>>>>> the first parameter 'if i write aaa in home page '
# --->> that means in the url to access the home page i write --> localhost:8000/aaa
# localhost:8000/about --> access the about page 
# the second one is the method inside the views (index) 
# third i set a name just to easly acces this path 
urlpatterns = [
    
    path('',views.index, name="index"),# this -- name -- can by used in navbar in {%url 'the path name'%}
    path ('about',views.about,name="about"), # the first parameter will be in the chrome url --> localhost:8080/'first_parameter'
]

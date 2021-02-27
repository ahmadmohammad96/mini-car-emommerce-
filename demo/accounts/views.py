from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User , AbstractBaseUser ,BaseUserManager 
from listings import *
from listings.models import *
from realtors import * 
from realtors.models import *
from accounts.models import Accounts
# from .form import Re
from .form import Fo
# Create your views here.

def login(request):
    # new_var2 = ''
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     new_que  = {'uu' : username }
    #     user = auth.authenticate(username=username,password=password)

    #     if user is not None:
    #         auth.login(request,user)
    #         # if auth.login(request,user) :

    #         # new_var2 = BaseUserManager..objects.all()
    #         # obj = new_var2.get(first_name=username)
    #         # bol = obj.active
    #         messages.success(request,'OK you are logged in ! ')
    #         ins_user = BaseUserManager
    #         # another_user = ins_user.get(first_name=username)

    #         # print(f'the active is -->> {bol}')

    #         return render(request,'pages/index.html' , new_que)
    #     else:
    #         messages.error(request,'Sorry invalid !!')
    #         return redirect('login')
       
    #     return redirect('login')
    # else:
    #     return render(request,'accounts/login.html')

    con = {}
    if request.session.has_key('username') : 
       return redirect('index')

    # if request.method == 'GET' :
    #     return render (request , 'accounts/login.html' , {})
    
    if request.method == 'POST':
        print('##########')
        take_name = request.POST.get('username') 
        take_password = request.POST.get('password')
        print(take_name , take_password)
        try:
            if Accounts.objects.all().get(username=take_name):
                print('inside the DB ')
                take_user = Accounts.objects.all().get(username=take_name)
                get_password = take_user.password
                if take_password == get_password:
                    request.session['username'] = take_name
                    request.session['password'] = take_password
                    return render(request , 'pages/index.html' , {})

                else:
                    con.update({'al' : 'Sorry the password you enterd is not working'})
                    # return render(request , 'partials/alert.html' , con)
                    raise ValueError('sorry ')

            else:
                con.update({'al' : 'Sorry the user is not in the Data Base'})
                # return render(request , 'partials/alert.html' , con)
                raise ValueError('sorry')

        except:
            pass


    return render(request , 'accounts/login.html' , {})
def register(request):
    pass
    # form = Re(request.POST or None)
    # if form.is_valid():
        # form.save()
    # if request.POST:
    #     the_realtor_name = request.POST['uname']
    #     # tmp_in_realtor = Realtor.objects.create_user(name=the_realtor_name)   
    #     the_realtor_name.save()
    # return render(request,'accounts/register.html',{'form':form})

    # else:
        # return render (request,'accounts/register.html')

    # if request.method == 'POST':
    #     first_name = request.POST['first_name']
    #     last_name =  request.POST['last_name']
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']

    #     if password == password2:
    #         if User.objects.filter(username=username).exists():
    #             messages.error(request,'Username is taken  !!')
    #             return redirect('register')
    #         else:
    #             if User.objects.filter(email=email):
    #                 messages.error(request,'Email is taken  !!')
    #                 return redirect('register')
    #             else:
    #                 user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
    #                 user.save()
    #                 messages.success(request,'OK you are registerd ! ')
    #                 return redirect('login')


    #     else:
    #         messages.error(request,'Passwords do NOT match !!')
    #         return redirect('register')

    # else:
    #     return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        return
    else:
        return redirect('index.html')


def dashboard(request):
    if request.method == 'POST':
        return
    else:
        
        return render(request,'accounts/dashboard.html')

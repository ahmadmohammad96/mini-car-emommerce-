from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(
        self , email , username , password=None ,
        is_active = True, is_staff=False , is_admin = False ,
        is_customer=False , is_realtor=False):

        if not email:
            raise ValueError('you must have an email')
        if not username:
            raise ValueError('you must have a username ')
        user = self.model(
            email = self.normalize_email(email) , 
            username = username

        )
        user.set_password(password)
        
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.customer = is_customer
        user.realtor = is_realtor


        user.save(using=self._db)
        return user

    def create_staffuser(self , email , username , password=None):
        user= self.create_user(
            email ,
            username = username , 
            password=password , 
            is_staff=True

        )
        return user

    def create_customeruser(self , email , username , password=None):
        user= self.create_user(
            email ,
            username = username , 
            password=password , 
            is_customer=True

        )
        return user   

    def create_realtoruser(self , email , username , password=None):
        user= self.create_user(
            email ,
            username = username , 
            password=password , 
            is_student=True

        )
        return user     

    def create_superuser(self , email , username , password=None ):
        user = self.create_user(
            email , 
            username = username , 
            password=password , 
            is_admin = True , 
            is_staff = True 


        )
      
      
        # user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    email = models.EmailField(max_length=60 , verbose_name='email' , unique=True)
    username = models.CharField(max_length=30 , unique=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined' , auto_now_add=True)
    last_login  = models.DateTimeField(verbose_name='Last Login' , auto_now=True) 
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    realtor = models.BooleanField(default=False)
    # superuser = models.BooleanField(default=True)
# ------------------------------------------------------------------------
    user_rate = models.IntegerField(blank=True , null=True)
    user_no_posts = models.IntegerField(blank=True , null=True)
    first_name = models.CharField(max_length=30 , verbose_name='First Name')
    lase_name = models.CharField(max_length=60 , verbose_name='Lase Name')

    punishments = models.TextField(blank=True , null=True)
    @property
    def is_customer(self):
        return self.customer


    @property
    def is_realtor(self):
        return self.realtor

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username' , ]
    objects = MyAccountManager()
    def __str__(self):
        return self.username

    def has_perm(self , perm , obj=None):
        return self.is_admin

    def has_module_perms(self , app_lebel):
        return True
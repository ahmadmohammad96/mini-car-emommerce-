from django import forms
from realtors.models import Realtor
# class Re(forms.ModelForm):
#     re_name = forms.CharField(max_length=100)
#     class meta:

#         model = Realtor
#         fields = ['name']
#         exclude = ['']
        
class Fo(forms.Form):
    user_name = forms.CharField(max_length=55)
    pass_word = forms.PasswordInput()
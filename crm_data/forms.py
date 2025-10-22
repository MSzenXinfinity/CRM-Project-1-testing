from django import forms

from crm_data.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        #fields='__all__'
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        #fields='__all__'
        fields=['user_id','address','profile_pic']
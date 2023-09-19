from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class Registro(UserCreationForm):
  
    username = forms.CharField(required=False,strip=False,widget=forms.TextInput(attrs={'autocomplete':'off','name':'username','id':'username','placeholder':'Username'}))
    email = forms.CharField(required=False,strip=False,widget=forms.TextInput(attrs={'autocomplete':'off','name':'email','id':'name','placeholder':'Email'}))
    password1 = forms.CharField(required=False,strip=False,widget=forms.PasswordInput(attrs={'id':'password1','name':'password1','placeholder':'Password'}))
    password2 = forms.CharField(required=False,strip=False,widget=forms.PasswordInput(attrs={'id':'password2','name':'password2','placeholder':'Confirm Password '}))
    
    
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']



class LoginAuthentication(AuthenticationForm):


    username = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off','name':'username','id':'username','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id':'password','name':'password','placeholder':'Password'}))
 

    class Meta:
        model = User
        fields = ['username','password']



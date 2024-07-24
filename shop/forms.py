from django import forms
from .models import User

class RegForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class':'form-control form-control-sm'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Your Email', 'class':'form-control form-control-sm'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Your city', 'class':'form-control form-control-sm'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'Your pasword', 'class':'form-control form-control-sm'}))
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'repeat pasword', 'class':'form-control form-control-sm'}))

    class Meta:
        model = User 
        fields = ['name','email','city','password','re_password']


class LogForm(forms.Form):
    UserName = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':'Your Name', 'class':'form-control form-control-sm'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder':'pasword', 'class':'form-control form-control-sm'}))
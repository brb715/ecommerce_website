from django import forms
from django.contrib.auth.models import User
from .models import Contact, Checkout


class signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        help_texts = {
            'username': None
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Must contain atleast 8 characters'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Should not contain characters'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class signin(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None
        }
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }


class contact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_no', 'issue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email Address'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'issue': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your issue.......', 'cols': '40', 'rows': '3'})
        }


class checkout(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = ['name', 'email', 'current_address',
                  'permament_address', 'phone_no', 'state', 'city', 'zip_code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'current_address': forms.TextInput(attrs={'class': 'form-control'}),
            'permament_address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'})
        }

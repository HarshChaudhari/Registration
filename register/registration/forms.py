#-*- coding: utf-8 -*-
from django import forms
from myapp.models import Profile

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

   def clean_message(self):
      username = self.cleaned_data.get("username")
      dbuser = Profile.objects.filter(name = name)

      if not dbuser:
         raise forms.ValidationError("User does not exist in our db!")
      return username

class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   lastName = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   passwordAgain = forms.CharField(widget = forms.PasswordInput())
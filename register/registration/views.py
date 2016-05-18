from django.shortcuts import render
from django.core.urlresolvers import reverse
from registration.forms import LoginForm,ProfileForm
from registration.models import Profile1

# Create your views here.
def SaveProfile(request):
   saved = False
   
   if request.method == "POST":
      MyProfileForm = ProfileForm(request.POST)

      if MyProfileForm.is_valid():
         profile1 = Profile1()
         profile1.name = MyProfileForm.cleaned_data["username"]
         profile1.lastName = MyProfileForm.cleaned_data["lastName"]
         password = MyProfileForm.cleaned_data["password"]
         passwordAgain = MyProfileForm.cleaned_data["passwordAgain"]
         profile1.password = password
        # profile1.picture = MyProfileForm.cleaned_data["picture"]
         profile1.save()
         saved = True

   else:
      MyProfileForm = ProfileForm()
		
   return render(request, 'saved.html', locals())


def login(request):
   username = "not logged in"
   
   if request.method == "POST":
      #Get the posted form
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         password1 = MyLoginForm.cleaned_data['password']
         if not Profile1.objects.filter(name=username).filter(password = password1):
                return render(request, 'login.html', {"error_message" : 'Incorrect username/password'})
                
   else:
      MyLoginForm = LoginForm()
		
   return render(request, 'loggedin.html', {"username" : username})

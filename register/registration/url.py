from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns('registration.views', 
   url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
   url(r'^login/', 'login', name = 'login'),
   url(r'^profile/',TemplateView.as_view(template_name = 'signup.html'),name = 'profile'), 
   url(r'^saved/', 'SaveProfile', name = 'saved'),
)

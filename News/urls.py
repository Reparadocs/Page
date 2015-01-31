from django.conf.urls import patterns, url
from News import views

urlpatterns = patterns('',
   
   url(r'^me/$', views.news, name='news'),
 
)
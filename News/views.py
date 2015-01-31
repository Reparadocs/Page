from django.shortcuts import render
from open_facebook import OpenFacebook
from django_facebook.api import get_facebook_graph
from django.http import HttpResponse

def news(request):
   if request.method == 'GET':
      graph = request.user.get_offline_graph()
      name = graph.fql('SELECT name FROM user WHERE uid = me()')

      return HttpResponse(name)


      

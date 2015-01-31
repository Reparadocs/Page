from django.shortcuts import render
from open_facebook import OpenFacebook
from django_facebook.api import get_facebook_graph

def news(request):
   if request.method == 'GET':
      graph = get_facebook_graph(request)
      return HttpResponse(graph.get('me'))


      

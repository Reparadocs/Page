from django.shortcuts import render
from open_facebook import OpenFacebook

def news(request):
   if request.method == 'GET':
      graph = get_facebook_graph(request)
      return HttpResponse(graph.get('me'))


      

from django.shortcuts import render
from open_facebook import OpenFacebook, FacebookConnection
from django_facebook.api import get_facebook_graph
from django.http import HttpResponse
import json

def news(request):
   if request.method == 'GET':
      graph = request.user.get_offline_graph()
      secgraph = get_facebook_graph(request)
      dicti = secgraph.get('/me/likes')
      data = FacebookConnection.request('/me/likes')
      return HttpResponse(json.dumps(dicti))

      

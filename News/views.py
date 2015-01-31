from django.shortcuts import render
from open_facebook import OpenFacebook, FacebookConnection
from django_facebook.api import get_facebook_graph
from django.http import HttpResponse
import json

def news(request):
   if request.method == 'GET':

      graph = request.user.get_offline_graph()
      return HttpResponse(graph.access_token))

      

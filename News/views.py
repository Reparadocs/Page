from django.shortcuts import render
from open_facebook import OpenFacebook, FacebookConnection
from django_facebook.api import get_facebook_graph, FacebookUserConverter
from django.http import HttpResponse
import json

def news(request):
   if request.method == 'GET':
      graph = request.user.access_token
      connection = FacebookConnection.request("/me/likes/",access_token=request.user.access_token)
      return HttpResponse(connection['data'])

      

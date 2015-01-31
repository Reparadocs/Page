from django.shortcuts import render
from open_facebook import OpenFacebook, FacebookConnection
from django_facebook.api import get_facebook_graph, FacebookUserConverter
from django.http import HttpResponse
import json

def news(request):
   if request.method == 'GET':
      graph = request.user.get_offline_graph()
      return HttpResponse(request.user.access_token)
      likes_response = graph.get('me/likes', limit=100)
      likes = likes_response and likes_response.get('data')
      return HttpResponse(likes)

      

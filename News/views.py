from django.shortcuts import render
from pybing import Bing

def news(request):
   if request.method == 'GET':
      bing = Bing('
      

# Django
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Django REST Framework
#from rest_framework import viewsets, mixins

# Scripts
# from scripts.foursquare import *

# Python
import oauth2 as oauth
import simplejson as json
import requests

# Models
from hackathon.models import *
from hackathon.serializers import SnippetSerializer
from hackathon.forms import UserForm


def synesthize(request):
    print "synesthize: " + str(request.user)
      
    context = {'hello': 'world'}
    return render(request, 'templates/hackathon/synesthize.html', context)

def index(request):
    print "index: " + str(request.user)
      
    context = {'hello': 'world'}
    return render(request, 'templates/hackathon/synesthize.html', context)


'''
#########################
# Snippet RESTful Model #
#########################

class CRUDBaseView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    pass


class SnippetView(CRUDBaseView):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()
'''

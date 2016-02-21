from django.shortcuts import render_to_response, redirect
from django.contrib.auth import logout as auth_logout
import urllib, urllib2, cookielib
from linkedin.linkedin import (LinkedInAuthentication, LinkedInApplication)
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
import json
import requests

API_KEY = u'7522okfvc7gkp8'
API_SECRET = u'dQqSsfyiW0H7a2BP'

class LinkedInWrapper(object):
    """ Simple namespacing """

    authentication = LinkedInAuthentication(API_KEY, API_SECRET, 'http://127.0.0.1:8000/get_access_token', ['r_basicprofile'])
    application = LinkedInApplication(authentication)

liw = LinkedInWrapper()
global access_token

def login(request):
    return redirect(liw.authentication.authorization_url)

def home(request):
    return render_to_response('home.html', context=RequestContext(request))

def logout(request):
    auth_logout(request)
    return redirect('/login')

@csrf_exempt
def get_access_token(request):
    global access_token
    """url = 'https://www.linkedin.com/uas/oauth2/accessToken'
    values = {'grant_type': 'authorization_code', 'code':request.GET["code"],
                  'redirect_uri':'http://127.0.0.1:8000/home', 'client_id':API_KEY,
                  'client_secret':API_SECRET}
    req = urllib2.Request(url, data=json.dumps(values))
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(req)"""
    #res = requests.post(url, data=values, headers={'Content-Type':'application/x-www-form-urlencoded'})
    #assert res.status_code == requests.codes.ok
    liw.authentication.authorization_code = request.GET['code']
    #liw.authentication.redirect_uri = 'http://127.0.0.1:8000/home'
    access_token = liw.authentication.get_access_token()
    #return redirect(liw.authentication.get_access_token())
    return redirect("/connections")

def connections(request):
    global access_token
    return render_to_response('connections.html', context=RequestContext(request, {'access_token':access_token[0]}))

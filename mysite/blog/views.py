from django.shortcuts import render,redirect

from django.utils import timezone

from .models import Captcha
from .forms import Captchaform

from django.contrib.auth.decorators import user_passes_test

from requests_oauthlib import OAuth1
import json
import requests
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

#####last searched persons ##########
def last_search(request):
    posts = Captcha.objects.all()
    return render(request, 'last_search.html', {'posts':posts})

def detail(request, pk):
    posts = Captcha.objects.get(pk=pk)
    return render(request, 'details.html', {'posts': posts})

############ details saving and captcha ####################

@user_passes_test(lambda u: u.is_superuser)
def home(request):

    try:
    	if request.method == "POST":
           form = Captchaform(request.POST)
           post = form.save(commit=False)
           if form.is_valid():
              post.published_date = timezone.now()
              post.save()
              return redirect('twitterapp')
        else:
           form = Captchaform()
        return render(request, 'home.html', {'form': form})

    except:
           return redirect('error')

 ########### for twitter App ###########

def twitterapp(request):
    return render(request, 'twitterapp.html',{})


def tweets(request):
    if request.method == 'POST':
       twitter_id = request.POST.get('screen_name','')
       num = request.POST.get('count','')

       auth = OAuth1('TxHMFbTrXLoxGwdNi9EENKFzN',
                     'OX8dvppxFGiviPZEzecpPKkpkm8j0hnWhwtWETuNEGB4fk2AEc',
                     '1889500886-qIkta3TT3tLt16AI4u0j6rqi9dXCUhR9QFZlylm',
                     'CrAJxzP1NU9lKbQOv8ijAHFO8eWd7FljtblNmnTxxQlGX')
       lis = []
       r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name='+twitter_id+'&count='+num,auth=auth)

       us = r.json()
       num = int(num)
       for i in range(num):

           lis.append(us[i]["text"])
       return render(request, 'tweets.html', {'tweets':lis})

######## error ###########

def error(request):
    return render(request, 'error.html',{})

def about(request):
    return render(request, 'about.html', {})

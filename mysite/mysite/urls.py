"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin

from blog.views import index, home,tweets,twitterapp,last_search,error,detail, about

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ########## Project ############
    url(r'^$', index, name='index'),
    url(r'^home/', home, name='home'),
     ######### twitter ###########
    url(r'^tweets/', tweets, name='tweets'),
    url(r'^twitterapp/', twitterapp, name='twitterapp'),

    ####### last search ############
    url(r'^(?P<pk>\d+)/$', detail, name='detail'),
    url(r'^last_search/', last_search, name='last_search'),
    url(r'^about/', about, name='about'),
    ######### error ######
    url(r'^error/', error, name='error'),

    ######## registration ###########
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

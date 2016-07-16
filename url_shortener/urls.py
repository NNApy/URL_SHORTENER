from django.conf.urls import url
from django.contrib import admin

from my_shortener.views import index, save_url

urlpatterns = [
    url(r'^save/', save_url, name = 'save_url'),
    url(r'^$', index, name = 'index'),

]

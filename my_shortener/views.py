import random
import string
import time

from django.shortcuts import render, redirect
from forms import UrlForm
from models import Urls


def index(request):

    if request.GET.get('s'):
        url = Urls.objects.filter(short_url=request.GET.get('s')).get()
        Urls.objects.filter(short_url=request.GET.get('s')).update(click_numbers = url.click_numbers + 1)
        return redirect(url.protocol + url.long_url)
    context = {'urls_data': Urls.objects.filter().order_by('-id'),
               'server_url': '127.0.0.1:8000?s='}
    return render(request, 'index.html', context)


def save_url(request):
    form = UrlForm(request.POST)
    if form.is_valid():
        long_u = request.POST.get('long_url').strip().strip('/')
        short_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))
        while Urls.objects.filter(short_url=short_url):
            short_url = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(6))

        used_protocol = 'http://'
        protocols = ['http://', 'https://', 'ftp://']
        for p in protocols:
            if p in long_u:
                used_protocol = p
                long_u = long_u.replace(used_protocol, '')

        Urls.objects.create(protocol=used_protocol,
                        long_url = long_u,
                        create_date=time.strftime("%Y %b %d"),
                        short_url=short_url)

        return redirect(index)

    else:
        context = {'urls_data': Urls.objects.filter().order_by('-id'),
                   'server_url': '127.0.0.1:8000?s=',
                   'message': 'Oops, Your URL is not valid. Please, try again...'}
        return render(request, 'index.html', context)
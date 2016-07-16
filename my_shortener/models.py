from __future__ import unicode_literals

from django.db import models


class Urls(models.Model):
    protocol = models.CharField(max_length=8, default='http://')
    long_url = models.CharField(max_length=100)
    create_date = models.CharField(max_length=10)
    short_url = models.CharField(max_length=10)
    click_numbers = models.IntegerField(default = 0)

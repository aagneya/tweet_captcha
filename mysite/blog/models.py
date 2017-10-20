from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Captcha(models.Model):
    
    first = models.CharField(max_length=25,null=True)
    last = models.CharField(max_length=25,null=True)   
    email = models.EmailField(max_length=70,null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first



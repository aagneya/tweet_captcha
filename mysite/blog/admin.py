from django.contrib import admin

# Register your models here.

from .models import Captcha

admin.site.register(Captcha)

from django import forms

from captcha.fields import ReCaptchaField

from .models import Captcha

class Captchaform(forms.ModelForm):
    
    captcha = ReCaptchaField()
    class Meta:
        model = Captcha
        fields = ('first','last','email',)




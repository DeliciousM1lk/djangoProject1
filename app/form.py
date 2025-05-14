from django.forms import *
from .models import *


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ['rubric', 'title', 'content', 'price']


class ContactForm(forms.Form):
    name = CharField(label='Имя', max_length=30)
    email = EmailField(label='Email')
    text = CharField(label='Сообщение', max_length=500, widget=Textarea)

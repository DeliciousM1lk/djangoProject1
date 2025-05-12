from django.forms import *
from .models import *


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ['rubric','title','content','price']




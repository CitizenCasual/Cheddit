from django.forms import ModelForm
from .models import Thread

class ThreadForm(ModelForm):
  class Meta:
    model = Thread
    fields = ['title', 'body', 'header_image']
from django import forms
from .models import News


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views', 'news_instance')


class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views', 'news_instance')



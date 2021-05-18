from django import forms
from .models import News
from reader.models import Reader


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views', 'news_instance')


class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ('views', 'news_instance')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Reader
        exclude = ('is_author',)
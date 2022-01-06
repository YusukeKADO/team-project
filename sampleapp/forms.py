from django import forms
from PIL import Image

from .models import Article, Media

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title',
            'body',
        )
        widgets = {
            'title':forms.Textarea(
                attrs = {'rows':1, 'cols':16, 'placeholder':'タイトルを入力'}
            ),
            'body': forms.Textarea(
                attrs = {'rows':4, 'cols':16, 'placeholder':'ここに入力'}
            ),
        }

class MediaCreateForm(forms.Form):
    picture = forms.ImageField(required=True)        
from django import forms

from .models import Article

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'body',
        )
        widgets = {
            'body': forms.Textarea(
                attrs = {'rows':16, 'cols':36, 'placeholder':'ここに入力'}
            ),
        }
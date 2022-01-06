from django import forms

from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'introduction',
            'Twitter_ID',
        )
        widgets = {
            'email':forms.Textarea(
                attrs = {'rows':1, 'cols':40, 'placeholder':'メールアドレスを入力'}
            ),
            'introduction': forms.Textarea(
                attrs = {'rows':4, 'cols':30, 'placeholder':'自己紹介を入力'}
            ),
            'Twitter_ID': forms.Textarea(
                attrs = {'rows':1, 'cols':15, 'placeholder':'Twitter_IDを入力'}
            ),
            'Facebook_URL': forms.Textarea(
                attrs = {'rows':1, 'cols':100, 'placeholder':'FacebookのURLを入力'}
            ),
            'Instagram_ID': forms.Textarea(
                attrs = {'rows':1, 'cols':15, 'placeholder':'Instagram_IDを入力'}
            ),
            'TikTok_ID': forms.Textarea(
                attrs = {'rows':1, 'cols':15, 'placeholder':'TikTok_IDを入力'}
            ),
        }
from django import forms

from .models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'introduction',
        )
        widgets = {
            'email':forms.Textarea(
                attrs = {'rows':1, 'cols':40, 'placeholder':'メールアドレスを入力'}
            ),
            'introduction': forms.Textarea(
                attrs = {'rows':4, 'cols':30, 'placeholder':'自己紹介'}
            ),
        }
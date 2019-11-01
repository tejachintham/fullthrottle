from django import forms
from mainpage.models import Post


class HomeForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Search a term...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
from django import forms
from News.models import NewsPosts


class AddNews(forms.ModelForm):
    class Meta:
        model = NewsPosts
        exclude = {'slug', 'user'}
        fields = ['title', 'description', 'body', 'category', 'cover_picture', 'speaker']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control', 'width': '650px'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'cover_picture': forms.FileInput(attrs={'class': 'form-control'}),
            'speaker': forms.TextInput(attrs={'class': 'form-control'}),
        }
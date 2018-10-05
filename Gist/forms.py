from django import forms
from Gist.models import GistPost


class Addgist(forms.ModelForm):
    class Meta:
        model = GistPost
        exclude = {'slug', 'user'}
        fields = ['title', 'body', 'category', 'seo_title', 'description', 'cover_image',
                  'poster']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'seo_title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'poster': forms.TextInput(attrs={'class': 'form-control'}),
        }
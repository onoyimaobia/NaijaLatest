from django import forms
from .models import Profile
#from Profile.validator import file_size
from django.core.files.images import get_image_dimensions
from django.contrib import admin
from django import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


#class myForm(forms.ModelForm):
   #class Meta:
       #model = myModel
   #def clean_picture(self):
       #picture = self.cleaned_data.get("picture")
       #if not picture:
           #raise forms.ValidationError("No image!")
       #else:
          # w, h = get_image_dimensions(picture)
           #if w != 100:
               #raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
          # if h != 200:
               #raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
       #return picture


class ProfilePic(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('address', 'contact_number', 'profile_picture')

        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'required':False}),
        }

        def clean_content(self):
            content = self.cleaned_data['profile_picture']
            content_type = content.content_type.split('/')[0]
            if content_type in settings.CONTENT_TYPES:
                if content.size > settings.MAX_UPLOAD_SIZE:
                    raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (
                    filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content.size)))
            else:
                raise forms.ValidationError(_('File type is not supported'))
            return content

    """def clean_picture(self):
        profile_picture = self.cleaned_data.get("profile_picture")
        if not profile_picture:
            raise forms.ValidationError("No image!")
        else:
            w, h = get_image_dimensions(profile_picture)
            if w != 100:
                raise forms.ValidationError("The image is %i pixel wide. It's supposed to be 100px" % w)
            if h != 200:
                raise forms.ValidationError("The image is %i pixel high. It's supposed to be 200px" % h)
        return profile_picture"""
from django import forms

from .models import Corpusobject

class PostForm(forms.ModelForm):

    class Meta:
        model = Corpusobject
        fields = ('name', 'catid', 'verbsaddress', 'language', 'project', 'knownloc', 'physical', 'downloadable', 'project')
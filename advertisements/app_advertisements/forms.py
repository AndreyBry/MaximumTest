from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisement


# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control from-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control from-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control from-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control from-control-lg'}))

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control from-control-lg'}),
            'description': forms.Textarea(attrs={'class': 'form-control from-control-lg'}),
            'price': forms.NumberInput(attrs={'class': 'form-control from-control-lg'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control from-control-lg'})
        }

    def clean_title(self):
        data = self.cleaned_data['title']
        if data.startswith('?'):
            raise ValidationError("Заголовок не может начинаться с вопросительного знака")
        return data

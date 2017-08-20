from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from front_site.models import User, Company, Events


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['geo', 'name']

    def __init__(self, *args, **kwargs):
        super(CreateCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Company name'})
        self.fields['geo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Geo location'})


class UpdateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['geo', 'name']

    def __init__(self, *args, **kwargs):
        super(UpdateCompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Company name'})
        self.fields['geo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Geo location'})


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['name', 'description', 'time_start', 'time_end', 'geo', 'img']

    def __init__(self, *args, **kwargs):
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Event name'})
        self.fields['geo'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Geo location'})
        self.fields['time_start'].widget.attrs.update({'class': 'begin'})
        self.fields['time_end'].widget.attrs.update({'class': 'end'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Event decription'})
        self.fields['img'].widget.attrs.update({'class': 'upload', 'placeholder': 'Download image'})

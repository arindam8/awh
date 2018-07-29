
from django import forms


class EnquiryForm(forms.Form):
    CHOICES = (
        ('Developer', 'Developer'),
        ('Architect', 'Architect'),
        ('Neighbour', 'Neighbour'),
        ('Other', 'Other'),

    )

    name=forms.CharField(label="Name",max_length=1000,widget = forms.TextInput(attrs={'id':'name','class': "form-control"}))
    email = forms.EmailField(label="Email",widget = forms.TextInput(attrs={'id':'email','class': "form-control"}))
    description = forms.CharField(label="Description",max_length=1000,widget = forms.Textarea(attrs={'id':'comment','rows':'1','class': "form-control"}))
    postcode = forms.CharField(label="Postcode",max_length=100,widget = forms.TextInput(attrs={'id':'postcode','class': "form-control"}))
    attach = forms.Field(label="Attachment",widget = forms.FileInput(attrs={'class': "form-control"}))
    phone = forms.CharField(label="Phone",widget = forms.TextInput(attrs={'id':'number','class': "form-control"}))
    category=forms.ChoiceField(label="Category",choices=CHOICES,widget = forms.RadioSelect(attrs={'class': "form-control enquire_radio_circle"}))
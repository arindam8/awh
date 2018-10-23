from django import forms

class EnquiryForm(forms.Form):
    CHOICES = (
        ('Developer', 'Developer'),
        ('Architect', 'Architect'),
        ('Neighbour', 'Neighbour'),
        ('Other', 'Other'),
    )

    name = forms.CharField(label="Name",max_length=1000,widget = forms.TextInput(attrs={'placeholder':'Full Name','id':'name','class': "form-control"}))
    email = forms.EmailField(label="Email",required=False,widget = forms.TextInput(attrs={'placeholder':'E-mail','id':'email','class': "form-control"}))
    description = forms.CharField(label="Description",max_length=1000,widget = forms.Textarea(attrs={'placeholder':'Description e.g. Development Type, Planning Application Number, etc...','rows':'1','class': "form-control comment"}))
    postcode = forms.CharField(label="Postcode",max_length=100,widget = forms.TextInput(attrs={'placeholder':'Postcode','id':'postcode','class': "form-control"}))
    attach = forms.Field(label="Attachment",required=False,widget = forms.FileInput(attrs={'placeholder':'Attachment','class': "form-control id_attach",'id':'id_attach'}))
    phone = forms.CharField(label="Phone",required=False,widget = forms.TextInput(attrs={'placeholder':'Phone Number','id':'number','class': "form-control"}))
    category=forms.ChoiceField(label="Category",choices=CHOICES,widget = forms.RadioSelect(attrs={'placeholder':'Category','class': "form-control enquire_radio_circle"}))

    def clean(self):

        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if (email=='' and phone==''):
            msg = forms.ValidationError("One of the fields is required")
            self.add_error('email', msg)

        return self.cleaned_data

class EnquiryFormPopUp(forms.Form):
    CHOICES = (
        ('Developer', 'Developer'),
        ('Architect', 'Architect'),
        ('Neighbour', 'Neighbour'),
        ('Other', 'Other'),
    )

    name = forms.CharField(label="Name",max_length=1000,widget = forms.TextInput(attrs={'placeholder':'Full Name','id':'name','class': "form-control"}))
    email = forms.EmailField(label="Email",required=False,widget = forms.TextInput(attrs={'placeholder':'E-mail','id':'email','class': "form-control"}))
    description = forms.CharField(label="Description",max_length=1000,widget = forms.Textarea(attrs={'placeholder':'Description e.g. Development Type, Planning Application Number, etc...','id':'comment','rows':'1','class': "form-control comment"}))
    postcode = forms.CharField(label="Postcode",max_length=100,widget = forms.TextInput(attrs={'placeholder':'Postcode','id':'postcode','class': "form-control"}))
    attach = forms.Field(label="Attachment",required=False,widget = forms.FileInput(attrs={'placeholder':'Attachment','class': "form-control id_attach",'id':'id_attach_pop'}))
    phone = forms.CharField(label="Phone",required=False,widget = forms.TextInput(attrs={'placeholder':'Phone Number','id':'number','class': "form-control"}))
    category=forms.ChoiceField(label="Category",choices=CHOICES,widget = forms.RadioSelect(attrs={'placeholder':'Category','class': "form-control enquire_radio_circle"}))

    def clean(self):

        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if (email=='' and phone==''):
            msg = forms.ValidationError("One of the fields is required")
            self.add_error('email', msg)

        return self.cleaned_data
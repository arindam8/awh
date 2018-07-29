# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
import json
from django.shortcuts import render
from .forms import EnquiryForm

def get_credentials():
    with open('awh_build/configuration/config.json') as f:
        data = json.load(f)

    creds={'email':data['email_host'],'password':data['email_password']}
    return (creds)






def base_view(request):
    if request.method != 'POST':
        form = EnquiryForm()
        return render(request,'home/base.html', {'enquiry_form': form})

    form = EnquiryForm(request.POST, request.FILES)
    if form.is_valid():
        description = form.cleaned_data['description']
        postcode = form.cleaned_data['postcode']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        attach = request.FILES['attach']
        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, [email])
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            return render(request,'home/base.html', {'message': 'Sent email to %s' % email})
        except:
            return render(request,'home/base.html', {'message': 'Either the attachment is too  big or corrupt'})


        return render(request,'home/base.html', {'message': 'Unable to send email. Please try again later'})


def rol_view(request):
    return render_to_response('home/template_category.html')

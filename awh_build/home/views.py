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


        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, [email])
            if len(request.FILES) != 0:
                attach = request.FILES['attach']
                mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            return render(request,'home/base.html', {'message': 'Thanks for the enquiry. We will be in touch shortly'})
        except:
            return render(request,'home/base.html', {'message': 'Either the attachment is too  big or corrupt'})


        return render(request,'home/base.html', {'message': 'Unable to send email. Please try again later'})

    return render(request, 'home/base.html', {'enquiry_form': form})


def rol_view(request,index=-99):
    if index=='0':
        return render(request, 'home/template_category.html',{'index':-99})
    else:
        return render(request, 'home/template_category.html',{'index':index})

def about_view(request):
    return render(request, 'home/about.html')

def case_studies_view(request,index=-99):

    return render(request, 'home/case_studies.html',{'index':index})


def dos_view(request,index=-99):
    if index=='0':
        return render(request, 'home/dos.html',{'index':-99})
    else:
        return render(request, 'home/dos.html',{'index':index})

def pw_view(request,index=-99):
    if index=='0':
        return render(request, 'home/pw.html',{'index':-99})
    else:
        return render(request, 'home/pw.html',{'index':index})
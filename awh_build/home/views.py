# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
import json
from django.shortcuts import render
from .forms import EnquiryForm, EnquiryFormPopUp


def get_credentials():
    with open('awh_build/configuration/config.json') as f:
        data = json.load(f)

    creds={'email':data['email_host'],'password':data['email_password']}
    return (creds)

def base_view(request):
    if request.method != 'POST':
        form = EnquiryForm()
        form_pu = EnquiryFormPopUp()
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
    print ('here')
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
    else:
        print ('noowww')

    return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu})



def main(request):
    if request.method != 'POST':
        form = EnquiryForm()
        form_pu = EnquiryFormPopUp()
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
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
            form_p = EnquiryFormPopUp()
            return render(request,'home/base.html', {'message': 'Thanks for the enquiry. We will be in touch shortly','enquiry_form_pop_up':form_p})
        except:
            form_p = EnquiryFormPopUp()
            return render(request,'home/base.html', {'message': 'Either the attachment is too  big or corrupt','enquiry_form_pop_up':form_p})

        form_p = EnquiryFormPopUp()
        return render(request,'home/base.html', {'message': 'Unable to send email. Please try again later','enquiry_form_pop_up':form_p})
    form_p = EnquiryFormPopUp()
    return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_p})


def popup(request):
    if request.method != 'POST':
        form = EnquiryForm()
        form_pu = EnquiryFormPopUp()
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
    if form_pu.is_valid():
        description = form_pu.cleaned_data['description']
        postcode = form_pu.cleaned_data['postcode']
        phone = form_pu.cleaned_data['phone']
        email = form_pu.cleaned_data['email']


        name = form_pu.cleaned_data['name']
        category = form_pu.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, [email])
            if len(request.FILES) != 0:
                attach = request.FILES['attach']
                mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            form_p=EnquiryForm()
            return render(request,'home/base.html', {'message_pop_up': 'Thanks for the enquiry. We will be in touch shortly','enquiry_form':form_p})
        except:
            form_p = EnquiryForm()
            return render(request,'home/base.html', {'message_pop_up': 'Either the attachment is too  big or corrupt','enquiry_form':form_p})

        form_p=EnquiryForm()
        return render(request,'home/base.html', {'message_pop_up': 'Unable to send email. Please try again later','enquiry_form':form_p})
    form_p = EnquiryForm()
    return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form':form_p})




def about_view(request):
    form_pu = EnquiryFormPopUp()
    return render(request, 'home/about.html',{'enquiry_form_pop_up':form_pu})

def rol_view(request,index=-99):
    form_pu = EnquiryFormPopUp()
    if index=='0':
        return render(request, 'home/rol.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/rol.html',{'index':index,'enquiry_form_pop_up':form_pu})

def dos_view(request,index=-99):
    form_pu = EnquiryFormPopUp()
    if index=='0':
        return render(request, 'home/dos.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/dos.html',{'index':index,'enquiry_form_pop_up':form_pu})

def pw_view(request,index=-99):
    form_pu = EnquiryFormPopUp()
    if index=='0':
        return render(request, 'home/pw.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/pw.html',{'index':index,'enquiry_form_pop_up':form_pu})

def case_studies_view(request, index=-99):
    form_pu = EnquiryFormPopUp()
    return render(request, 'home/case_studies.html', {'index': index,'enquiry_form_pop_up':form_pu})
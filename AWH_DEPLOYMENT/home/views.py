# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
import json
from django.shortcuts import render
from .forms import EnquiryForm, EnquiryFormPopUp
# for twitter integration
import tweepy
import jsonpickle
# to create list from file
from ast import literal_eval


####################
# for dev purposes #
####################

import logging

fmt = getattr(settings, 'LOG_FORMAT', None)
lvl = getattr(settings, 'LOG_LEVEL', logging.DEBUG)

logging.basicConfig(format=fmt, level=lvl)

#####################

def get_credentials():
    with open('awh_build/configuration/config.json') as f:
        data = json.load(f)

    creds={'email':data['email_host'],'password':data['email_password']}
    return (creds)

def base_view(request):
    disp_tweets = get_tweets()
    disp_tweets = jsonpickle.encode(disp_tweets)

    if request.method != 'POST':

        form = EnquiryForm(initial={'category':'Developer'})
        form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu,'tweets':disp_tweets})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
    if form.is_valid():
        description = form.cleaned_data['description']
        postcode = form.cleaned_data['postcode']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']


        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category+"\n"+email
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, ['rightsoflight@awh.co.uk'])
            if len(request.FILES) != 0:
                attach = request.FILES['attach']
                mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            return render(request,'home/base.html', {'message': 'Thanks for the enquiry. We will be in touch shortly','tweets':disp_tweets})
        except:
            return render(request,'home/base.html', {'message': 'Either the attachment is too  big or corrupt','tweets':disp_tweets})


        return render(request,'home/base.html', {'message': 'Unable to send email. Please try again later','tweets':disp_tweets})
    else:

        return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu,'tweets':disp_tweets})



def main(request):
    disp_tweets = get_tweets()
    if request.method != 'POST':
        form = EnquiryForm(initial={'category':'Developer'})
        form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu,'tweets':disp_tweets})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
    if form.is_valid():
        description = form.cleaned_data['description']
        postcode = form.cleaned_data['postcode']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']


        name = form.cleaned_data['name']
        category = form.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category+"\n"+email
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, ['rightsoflight@awh.co.uk'])
            if len(request.FILES) != 0:
                attach = request.FILES['attach']
                mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            form_p = EnquiryFormPopUp(initial={'category':'Developer'})
            return render(request,'home/base.html', {'message': 'Thanks for the enquiry. We will be in touch shortly','enquiry_form_pop_up':form_p,'tweets':disp_tweets})
        except:
            form_p = EnquiryFormPopUp(initial={'category':'Developer'})
            return render(request,'home/base.html', {'message': 'Either the attachment is too  big or corrupt','enquiry_form_pop_up':form_p,'tweets':disp_tweets})

        form_p = EnquiryFormPopUp(initial={'category':'Developer'})
        return render(request,'home/base.html', {'message': 'Unable to send email. Please try again later','enquiry_form_pop_up':form_p,'tweets':disp_tweets})
    form_p = EnquiryFormPopUp(initial={'category':'Developer'})
    return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_p,'tweets':disp_tweets})


def popup(request):
    disp_tweets = get_tweets()
    if request.method != 'POST':
        form = EnquiryForm(initial={'category':'Developer'})
        form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
        return render(request,'home/base.html', {'enquiry_form': form,'enquiry_form_pop_up':form_pu,'tweets':disp_tweets})

    form = EnquiryForm(request.POST, request.FILES)
    form_pu = EnquiryFormPopUp(request.POST, request.FILES)
    if form_pu.is_valid():
        description = form_pu.cleaned_data['description']
        postcode = form_pu.cleaned_data['postcode']
        phone = form_pu.cleaned_data['phone']
        email = form_pu.cleaned_data['email']


        name = form_pu.cleaned_data['name']
        category = form_pu.cleaned_data['category']
        body=description+"\n"+name+"\n"+postcode+"\n"+phone+"\n"+category+"\n"+email
        try:
            mail = EmailMessage("AWH CUSTOMER ENQUIRY: URGENT!", body, settings.EMAIL_HOST_USER, ['rightsoflight@awh.co.uk'])
            if len(request.FILES) != 0:
                attach = request.FILES['attach']
                mail.attach(attach.name, attach.read(), attach.content_type)
            mail.send()
            form_p=EnquiryForm(initial={'category':'Developer'})
            return render(request,'home/base.html', {'message_pop_up': 'Thanks for the enquiry. We will be in touch shortly','enquiry_form':form_p,'tweets':disp_tweets})
        except:
            form_p = EnquiryForm(initial={'category':'Developer'})
            return render(request,'home/base.html', {'message_pop_up': 'Either the attachment is too  big or corrupt','enquiry_form':form_p,'tweets':disp_tweets})

        form_p=EnquiryForm()
        return render(request,'home/base.html', {'message_pop_up': 'Unable to send email. Please try again later','enquiry_form':form_p,'tweets':disp_tweets})
    form_p = EnquiryForm()
    return render(request, 'home/base.html', {'enquiry_form': form,'enquiry_form':form_p,'tweets':disp_tweets})




def about_view(request):
    form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
    return render(request, 'home/about.html',{'enquiry_form_pop_up':form_pu})

def rol_view(request,index=-99):
    form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
    if index=='0':
        return render(request, 'home/rol.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/rol.html',{'index':index,'enquiry_form_pop_up':form_pu})

def dos_view(request,index=-99):
    form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
    if index=='0':
        return render(request, 'home/dos.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/dos.html',{'index':index,'enquiry_form_pop_up':form_pu})

def pw_view(request,index=-99):
    form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
    if index=='0':
        return render(request, 'home/pw.html',{'index':-99,'enquiry_form_pop_up':form_pu})
    else:
        return render(request, 'home/pw.html',{'index':index,'enquiry_form_pop_up':form_pu})

def case_studies_view(request, index=-99):
    form_pu = EnquiryFormPopUp(initial={'category':'Developer'})
    return render(request, 'home/case_studies.html', {'index': index,'enquiry_form_pop_up':form_pu})


def get_tweets():
    # authentication
    auth = tweepy.OAuthHandler('8uY1nssYzWu0f8dF5MeREgqVr', '0V1KRinGxlEVXuvTWDHcbxpWTYLcZPta2yZ9jRHdjQSgtLvCe9')
    auth.set_access_token('1031669552541773826-G7vQXztmoyzCNIZozNGG8vq3zhLy8K', '6mAG4KAphfh7EXFbrykdI12r5lCvNb0QqYVi1OjlUjYed')
    # number of tweets to return
    tweetLimit = 3

    # try for rate limit error
    try:
        # get tweets
        api            = tweepy.API(auth)
        publicTweets   = api.home_timeline()

        # initiate
        tweets          = []
        shiftIndex      = tweetLimit
        tweetOffset     = 0

        # save tweets in list
        for tweet in publicTweets:
            tweetInfo            = {}
            tweetInfo['text']    = tweet.text
            tweetInfo['link_']   = tweet.entities['urls'][0]['expanded_url']
            tweetInfo['created'] = str(tweet.created_at)
            tweets.append(tweetInfo)
        # trim to 3 tweets
        tweets = tweets[:tweetLimit]

        # get old tweets from file
        with open('tweets.txt') as f:
            # parse file as list
            tweetsFromFile = [list(literal_eval(line)) for line in f]
        f.close()
        # parse first line as list
        tweetsFromFile = tweetsFromFile[0]

        # calculate number of tweets not loaded due to 7 day limit on API
        shiftIndex = shiftIndex - len(tweets)

        # calculate the number of new tweets loaded that overlap with the tweets loaded from the saved file
        for tweet in tweets:
            for savedTweet in tweetsFromFile:
                if tweet == savedTweet:
                    tweetOffset += 1

        # calculate index of last list item to append
        eol = tweetOffset + shiftIndex

        # shift and load tweets loaded from file to fill in lost data
        tweetsFromFile = tweetsFromFile[tweetOffset:eol]
        tweets.extend(tweetsFromFile)

        # write tweets to file
        f = open("tweets.txt", "w")
        f.write(str(tweets))
        f.close()

        # return tweets
        return (tweets)

    # handle rate limit error
    except:
        # load and return tweets from file
        with open('tweets.txt') as f:
            s = f.readline()
        f.close()

        # return tweets (parsed as list in a list?)
        return (s)


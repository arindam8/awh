# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response


def base_view(request):
    return render_to_response('home/base.html')


def rol_view(request):
    return render_to_response('home/template_category.html')

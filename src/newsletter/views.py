# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, ContactForm
import boto3
import json



def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    if request.user.is_authenticated():
        title = 'Hello %s' %(request.user)
        context = {
            "home_title" : title,
            "home_SignUpForm" : form
        }
    if form.is_valid():
        form.save()
    context = {
        "home_title" : "Thank you !"
    }

    # client = boto3.client('cloudformation')
    # with open('newsletter/cloudformationtest.json', 'r') as f:
    # 	response = client.create_stack(
    # 		StackName='stacktest',
    #     	TemplateBody=f.read()
    # 		)

    return render(request, "home.html", context)

    ##################################################
    # if not request.user.is_authenticated():
    #     form = SignUpForm()
    #     title = 'Welcome'
    #     context = {
    #         "template_title" : title,
    #         "template_SignUpForm" : form
    #     }
    #     return render(request, "home.html", context)
    # else:
    #     title = 'Hello %s' %(request.user)
    # context = {
    #     "template_title" : title
    # }
    # return render(request, "home.html", context)
def contact(request):
     form = ContactForm(request.POST or None)
     if form.is_valid():
         # for key, value in form.cleaned_data.iteritems():
         #     print key,value
         form_email = form.cleaned_data.get("email")
         form_message = form.cleaned_data.get("message")
         form_full_name = form.cleaned_data.get("full_name")

         subject = 'Site contact form'
         from_email = settings.EMAIL_HOST_USER
         to_email = [from_email, 'majdeddine.letaief@gmail.com']
         contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)

         send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

     context = {
        "contact_form" : form,
     }
     return render(request, "forms.html", context)


def defaultInfra(request):
    client = boto3.client('cloudformation')
    with open('newsletter/cloudformationtest.json', 'r') as f:
    	response = client.create_stack(
    		StackName='stacktest',
        	TemplateBody=f.read()
    		)

    return render(request, "home.html", {})

from __future__ import unicode_literals
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, ContactForm
import boto3
import json
###
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
    return render(request, "home.html", context)
###
def contact(request):
     form = ContactForm(request.POST or None)
     if form.is_valid():
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
###
def user(request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = 'Hello %s' %(request.user)
        context = {
            "home_title" : title,
        }
    return render(request, "user.html", context)
###
def cusInf_Basic(request):
    return render(request, "cusInf_Basic.html", {})
def cusInf_NACL(request):
    return render(request, "cusInf_NACL.html", {})
def cusInf_SG(request):
    return render(request, "cusInf_SG.html", {})
def cusInf_Instance(request):
    return render(request, "cusInf_Instance.html", {})
###
def defInf(request):
    title = 'Default Infrastructure'
    client = boto3.client('cloudformation')
    client1 = boto3.client('ec2')
    response = client.describe_stacks()
    global ip_add1, ip_add2
    for each in response['Stacks']:
        value = each['StackStatus']
        value1 = each['StackName']
        if value1 == 'tinyModel':
            response1= client.describe_stack_resources(
                StackName = 'tinyModel'
            )
            if value == 'CREATE_COMPLETE' and value1 == 'tinyModel' :
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add1 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add2= each['Instances'][0]['PublicIpAddress']
                context = {
                    "response" : value,
                    "response1" : value1,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2
                }

                print response
                return render(request, "defInf.html", context)
            else :
                context = {
                    "response" : value,
                }
                return render(request, "defInf.html", context)
        elif value1 == 'microModel':
            response1= client.describe_stack_resources(
                StackName = 'microModel'
            )
            if value == 'CREATE_COMPLETE' and value1 == 'microModel' :
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add1 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add2= each['Instances'][0]['PublicIpAddress']
                context = {
                    "response" : value,
                    "response1" : value1,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "response" : value,
                }
                return render(request, "defInf.html", context)
        elif value1 == 'mediumModel':
            response1= client.describe_stack_resources(
                StackName = 'mediumModel'
            )
            if value == 'CREATE_COMPLETE' and value1 == 'mediumModel' :
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add1 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add2= each['Instances'][0]['PublicIpAddress']
                context = {
                    "response" : value,
                    "response1" : value1,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "response" : value,
                }
                return render(request, "defInf.html", context)
        elif value1 == 'largeModel':
            response1= client.describe_stack_resources(
                StackName = 'largeModel'
            )
            if value == 'CREATE_COMPLETE' and value1 == 'largeModel' :
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add1 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add2= each['Instances'][0]['PublicIpAddress']
                context = {
                    "response" : value,
                    "response1" : value1,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "response" : value,
                }
                return render(request, "defInf.html", context)
        else :
            return render(request, "defInf.html", {})
###
def createDefInfra1(request):
    client = boto3.client('cloudformation')
    with open('newsletter/infraModels/tinyModel.json', 'r') as f:
    	response = client.create_stack(
    		StackName='tinyModel',
        	TemplateBody=f.read()
    		)
    return render(request, "user.html", {})

def createDefInfra2(request):
    client = boto3.client('cloudformation')
    with open('newsletter/infraModels/microModel.json', 'r') as f:
    	response = client.create_stack(
    		StackName='microModel',
        	TemplateBody=f.read()
    		)
    return render(request, "user.html", {})

def createDefInfra3(request):
    client = boto3.client('cloudformation')
    with open('newsletter/infraModels/mediumModel.json', 'r') as f:
    	response = client.create_stack(
    		StackName='mediumModel',
        	TemplateBody=f.read()
    		)
    return render(request, "user.html", {})

def createDefInfra4(request):
    client = boto3.client('cloudformation')
    with open('newsletter/infraModels/largeModel.json', 'r') as f:
    	response = client.create_stack(
    		StackName='largeModel',
        	TemplateBody=f.read()
    		)
    return render(request, "user.html", {})
###
def deleteInfra1(request):
    client = boto3.client('cloudformation')
    response = client.delete_stack(
        StackName='tinyModel',
    )
    return render(request, "user.html", {})

def deleteInfra2(request):
    client = boto3.client('cloudformation')
    response = client.delete_stack(
        StackName='microModel',
    )
    return render(request, "user.html", {})

def deleteInfra3(request):
    client = boto3.client('cloudformation')
    response = client.delete_stack(
        StackName='mediumModel',
    )
    return render(request, "user.html", {})

def deleteInfra4(request):
    client = boto3.client('cloudformation')
    response = client.delete_stack(
        StackName='largeModel',
    )
    return render(request, "user.html", {})

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ContactForm
from .models import DefaultStack, CustomStack
from .import forms
import os
import boto3
import json
#########################################################

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
#########################################################
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
#########################################################
@login_required
def user(request):
    return render(request, "user.html", {})
#########################################################
@login_required
def cusInf_Basic(request):
    if request.method == 'POST':
        form = forms.customInfra(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.infrastructure_owner = request.user
            instance.save()
        return redirect('cusInf_NACL')
    else :
        form = forms.customInfra()
        context = {
            "form":form,
        }
        return render(request, "cusInf_Basic.html", context)
#########################################################
@login_required
def cusInf_NACL(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    nacl = cs[number-1].infrastructure_nacl
    if request.method == 'POST':
        form = forms.nacl(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.nacl_name = str(request.user) + "NACL1"
            instance.save()
        return redirect('cusInf_SG')
    else :
        form = forms.nacl()
        context = {
            "form":form,
            "nacl":nacl,
        }
        return render(request, "cusInf_NACL.html", context)
#########################################################
@login_required
def cusInf_SG(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    sg = cs[number-1].infrastructure_sg
    if request.method == 'POST':
        form = forms.sg(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.sg_name = str(request.user) + "SG1"
            instance.save()
        return redirect('cusInf_Pub_Instance')
    else :
        form = forms.sg()
        context = {
            "form":form,
            "sg" : sg,
        }
        return render(request, "cusInf_SG.html", context)
#########################################################
@login_required
def cusInf_Pub_Instance(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    inst = cs[number-1].infrastructure_pubinst
    if request.method == 'POST':
        form = forms.instance(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return redirect('cusInf_Prv_Instance')
    else :
        form = forms.instance()
        context = {
            "form":form,
            "inst" : inst,
        }
    return render(request, "cusInf_Pub_Instance.html", context)

#########################################################
@login_required
def cusInf_Prv_Instance(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    inst = cs[number-1].infrastructure_prvinst
    if request.method == 'POST':
        form = forms.instance(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
        return redirect('cusInf_Prv_Instance')
    else :
        form = forms.instance()
        context = {
            "form":form,
            "inst" : inst,
        }
    return render(request, "cusInf_Prv_Instance.html", context)
#########################################################
@login_required
def createInfra(request):
    form = forms.createInfra()
    return render(request, "defInf.html", {"form" : form})
#########################################################
@login_required
def defInf(request):
    title = 'Default Infrastructure'
    client = boto3.client('cloudformation')
    client1 = boto3.client('ec2')
    client3 = boto3.client('autoscaling',region_name='eu-west-2')
    response = client.describe_stacks()
    global ip_add1, ip_add2
    ip_add1 = ''
    ip_add2 = ''
    ip_add3 = ''
    ip_add4 = ''
    if request.method == 'POST':
         form = forms.createInfra(request.POST)
         if form.is_valid() :
             instance = form.save(commit=False)
             instance.infrastructure_owner = request.user
             instance.save()
             context = {
                "from":form,
             }
             return render(request,"defInf.html",context)
    else:
        form = forms.createInfra()
    for each in response['Stacks']:
        value = each['StackStatus']
        value0 = each['StackName'].split('1')[1]
        value1 = value0.split('2')[0]
        value2 = each['StackName']
        value3 = value0.split('2')[1]
        if value1 == str(request.user) and value3 == 'tiny':
            response1 = client.describe_stack_resources(
                StackName = value2
            )
            if value == 'CREATE_COMPLETE':
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
                            ip_add2= each['Instances'][0]['PrivateIpAddress']
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "form" : form,
                }
                print value
                return render(request, "defInf.html", context)
        if value1 == str(request.user) and value3 == 'micro':
            response1= client.describe_stack_resources(
                StackName = value2
            )
            if value == 'CREATE_COMPLETE':
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2n1':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add1 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PublicEc2n2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add2 = each['Instances'][0]['PublicIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2n1':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add3= each['Instances'][0]['PrivateIpAddress']
                for each in response1['StackResources']:
                    if each['LogicalResourceId'] == 'PrivateEc2n2':
                        inst_id = each['PhysicalResourceId']
                        response2 = client1.describe_instances(Filters=[{'Name': 'instance-id','Values': [inst_id,]},],)
                        for each in response2['Reservations']:
                            ip_add4= each['Instances'][0]['PrivateIpAddress']
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "ip3" : ip_add3,
                    "ip4" : ip_add4,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
        if value1 == str(request.user) and value3 == 'medium':
            response1= client.describe_stack_resources(
                StackName = value2
            )
            if value == 'CREATE_COMPLETE':
                response2 = client1.describe_instances()
                for each in response2['Reservations']:
                    id = each['Instances'][0]['ImageId']
                    inst = each['Instances']
                    if id == 'ami-0708175939932fc75':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            for each in prv:
                                asso = each['Association']
                                ip_add1= asso['PublicIp']

                    if id == 'ami-00ee3b59e07408c27':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            ip_add2 = prv[0]['PrivateIpAddress']

                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
        if value1 == str(request.user) and value3 == 'large':
            response1= client.describe_stack_resources(
                StackName = value2
            )
            if value == 'CREATE_COMPLETE':
                response2 = client1.describe_instances()
                for each in response2['Reservations']:
                    id = each['Instances'][0]['ImageId']
                    inst = each['Instances']
                    if id == 'ami-0708175939932fc75':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            for each in prv:
                                asso = each['Association']
                                ip_add1= asso['PublicIp']

                    if id == 'ami-058f46b781900723c':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            for each in prv:
                                asso = each['Association']
                                ip_add2= asso['PublicIp']

                    if id == 'ami-00ee3b59e07408c27':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            ip_add3 = prv[0]['PrivateIpAddress']

                    if id == 'ami-049bd848e8c4021ad':
                        net = inst[0]['NetworkInterfaces']
                        for each in net:
                            prv = each['PrivateIpAddresses']
                            ip_add4 = prv[0]['PrivateIpAddress']

                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "ip3" : ip_add3,
                    "ip4" : ip_add4,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
            else :
                context = {
                    "val" : value,
                    "val1" : value1,
                    "val2" : value3,
                    "ip1" : ip_add1,
                    "ip2" : ip_add2,
                    "ip3" : ip_add3,
                    "ip4" : ip_add4,
                    "form" : form,
                }
                return render(request, "defInf.html", context)
        else :
            context = {
                "form" : form,
            }
            return render(request, "defInf.html", context)

    return render(request, "defInf.html", {"form" : form})
#########################################################
@login_required
def createDefInfra1(request):
    if request.method == 'POST':
        form = forms.createInfra(request.POST)
        client = boto3.client('cloudformation')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.infrastructure_owner = request.user
            instance.save()
            with open('newsletter/infraModels/tinyModel.json', 'r') as f:
            	response = client.create_stack(
            		StackName= "%s1%s2%s" %(instance.infrastructure_name,instance.infrastructure_owner,'tiny'),
                	TemplateBody=f.read()
            		)
            return render(request,"user.html",{})
    else:
        form = forms.createInfra()
        return render(request, "user.html", {'form':form})
#########################################################
@login_required
def createDefInfra2(request):
    if request.method == 'POST':
        form = forms.createInfra(request.POST)
        client = boto3.client('cloudformation')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.infrastructure_owner = request.user
            instance.save()
            with open('newsletter/infraModels/microModel.json', 'r') as f:
            	response = client.create_stack(
            		StackName= "%s1%s2%s" %(instance.infrastructure_name,instance.infrastructure_owner,'micro'),
                	TemplateBody=f.read()
            		)
            return render(request,"user.html",{})
    else:
        form = forms.createInfra()
        return render(request, "user.html", {'form':form})
#########################################################
@login_required
def createDefInfra3(request):
    if request.method == 'POST':
        form = forms.createInfra(request.POST)
        client = boto3.client('cloudformation')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.infrastructure_owner = request.user
            instance.save()
            with open('newsletter/infraModels/mediumModel.json', 'r') as f:
            	response = client.create_stack(
            		StackName= "%s1%s2%s" %(instance.infrastructure_name,instance.infrastructure_owner,'medium'),
                	TemplateBody=f.read()
            		)
            return render(request,"user.html",{})
    else:
        form = forms.createInfra()
        return render(request, "user.html", {'form':form})
#########################################################
@login_required
def createDefInfra4(request):
    if request.method == 'POST':
        form = forms.createInfra(request.POST)
        client = boto3.client('cloudformation')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.infrastructure_owner = request.user
            instance.save()
            with open('newsletter/infraModels/largeModel.json', 'r') as f:
            	response = client.create_stack(
            		StackName= "%s1%s2%s" %(instance.infrastructure_name,instance.infrastructure_owner,'large'),
                	TemplateBody=f.read()
            		)
            return render(request,"user.html",{})
    else:
        form = forms.createInfra()
        return render(request, "user.html", {'form':form})
#########################################################
@login_required
def deleteInfra1(request):
    client = boto3.client('cloudformation')
    response1 = client.describe_stacks()
    for each in response1['Stacks']:
        value = each['StackName']
        response = client.delete_stack(StackName= value,)
    return render(request, "user.html", {})
#########################################################
@login_required
def deleteInfra2(request):
    client = boto3.client('cloudformation')
    response1 = client.describe_stacks()
    for each in response1['Stacks']:
        value = each['StackName']
        response = client.delete_stack(StackName= value,)
    return render(request, "user.html", {})
#########################################################
@login_required
def deleteInfra3(request):
    client = boto3.client('cloudformation')
    response1 = client.describe_stacks()
    for each in response1['Stacks']:
        value = each['StackName']
        response = client.delete_stack(StackName= value,)
    return render(request, "user.html", {})
#########################################################
@login_required
def deleteInfra4(request):
    client = boto3.client('cloudformation')
    response1 = client.describe_stacks()
    for each in response1['Stacks']:
        value = each['StackName']
        response = client.delete_stack(StackName= value,)
    return render(request, "user.html", {})

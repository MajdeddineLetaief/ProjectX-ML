from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ContactForm
from .models import DefaultStack, CustomStack, NACL,NACL2,NACL3,NACL4, SG,SG2,SG3,SG4, Instance,Instance2,Instance3,Instance4
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

def about(request):

    return render(request, "about.html", {})
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
########################
########################
#########################################################
@login_required
def cusInf_Basic(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    if number != 0 :
        owner = cs[0].infrastructure_owner
        user = request.user
        ip= []
        ip2= []
        ip3= []
        ip4= []
        if owner == request.user :
            infra_name = cs[number-1].infrastructure_name
            inst_number = cs[number-1].infrastructure_pubinst
            if str(inst_number) == "1":
                client = boto3.client('ec2')
                response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
                for each in response['Reservations']:
                    ip_add= each['Instances'][0]['PublicIpAddress']
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
                            "number":number,
                            "infra_name":infra_name,
                            "ip_add":ip_add,
                            "inst_number":inst_number,
                            "owner":owner,
                            "user":user,
                        }
                        print ip_add
                        return render(request, "cusInf_Basic.html", context)
            if str(inst_number) == "2":
                client = boto3.client('ec2')
                response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
                response2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
                for each in response['Reservations']:
                    ipadd = each['Instances'][0]['PublicIpAddress']
                    ip.append(ipadd)
                for each in response2['Reservations']:
                    ipadd2 = each['Instances'][0]['PublicIpAddress']
                    ip2.append(ipadd2)
                ip_add = ip[0]
                ip_add2 = ip2[0]
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
                        "number":number,
                        "infra_name":infra_name,
                        "ip_add":ip_add,
                        "ip_add2":ip_add2,
                        "inst_number":inst_number,
                        "owner":owner,
                        "user":user,
                    }
                    return render(request, "cusInf_Basic.html", context)
            if str(inst_number) == "3":
                client = boto3.client('ec2')
                response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
                response2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
                response3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
                for each in response['Reservations']:
                    ipadd = each['Instances'][0]['PublicIpAddress']
                    ip.append(ipadd)
                for each in response2['Reservations']:
                    ipadd2 = each['Instances'][0]['PublicIpAddress']
                    ip2.append(ipadd2)
                for each in response3['Reservations']:
                    ipadd3 = each['Instances'][0]['PublicIpAddress']
                    ip3.append(ipadd3)
                ip_add = ip[0]
                ip_add2 = ip2[0]
                ip_add3 = ip3[0]
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
                        "number":number,
                        "infra_name":infra_name,
                        "ip_add":ip_add,
                        "ip_add2":ip_add2,
                        "ip_add3":ip_add3,
                        "inst_number":inst_number,
                        "owner":owner,
                        "user":user,
                    }
                    return render(request, "cusInf_Basic.html", context)
            if str(inst_number) == "4":
                client = boto3.client('ec2')
                response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
                response2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
                response3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
                response4 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance4',]},{'Name':'instance-state-name','Values':['running',]},],)
                for each in response['Reservations']:
                    ipadd = each['Instances'][0]['PublicIpAddress']
                    ip.append(ipadd)
                for each in response2['Reservations']:
                    ipadd2 = each['Instances'][0]['PublicIpAddress']
                    ip2.append(ipadd2)
                for each in response3['Reservations']:
                    ipadd3 = each['Instances'][0]['PublicIpAddress']
                    ip3.append(ipadd3)
                for each in response4['Reservations']:
                    ipadd4 = each['Instances'][0]['PublicIpAddress']
                    ip4.append(ipadd4)
                ip_add = ip[0]
                ip_add2 = ip2[0]
                ip_add3 = ip3[0]
                ip_add4 = ip4[0]
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
                        "number":number,
                        "infra_name":infra_name,
                        "ip_add":ip_add,
                        "ip_add2":ip_add2,
                        "ip_add3":ip_add3,
                        "ip_add4":ip_add4,
                        "inst_number":inst_number,
                        "owner":owner,
                        "user":user,
                    }
                    return render(request, "cusInf_Basic.html", context)
        else :
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
                    "number":number,
                }
                return render(request, "cusInf_Basic.html", context)
    else :
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
                "number":number,
            }
            return render(request, "cusInf_Basic.html", context)
#########################################################
@login_required
def cusInf_NACL(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    nacl = cs[number-1].infrastructure_nacl
    infra_name = cs[number-1].infrastructure_name
    nacl_number = cs[number-1].infrastructure_nacl
    if str(nacl_number) == "1":
        if request.method == 'POST':
            form = forms.nacl(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.nacl_name = str(request.user) + "NACL1"
                instance.nacl_infra = infra_name
                instance.nacl_owner = request.user
                instance.save()
            return redirect('cusInf_SG')
        else :
            form = forms.nacl()
            context = {
                "form":form,
                "nacl":nacl,
            }
            return render(request, "cusInf_NACL.html", context)
    if str(nacl_number) == "2":
        if request.method == 'POST':
            form = forms.nacl2(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.nacl_name = str(request.user) + "NACL1"
                instance.nacl_infra = infra_name
                instance.nacl_owner = request.user
                instance.save()
            return redirect('cusInf_SG')
        else :
            form = forms.nacl2()
            context = {
                "form":form,
                "nacl":nacl,
            }
            return render(request, "cusInf_NACL.html", context)
    if str(nacl_number) == "3":
        if request.method == 'POST':
            form = forms.nacl3(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.nacl_name = str(request.user) + "NACL1"
                instance.nacl_infra = infra_name
                instance.nacl_owner = request.user
                instance.save()
            return redirect('cusInf_SG')
        else :
            form = forms.nacl3()
            context = {
                "form":form,
                "nacl":nacl,
            }
            return render(request, "cusInf_NACL.html", context)
    if str(nacl_number) == "4":
        if request.method == 'POST':
            form = forms.nacl4(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.nacl_name = str(request.user) + "NACL1"
                instance.nacl_infra = infra_name
                instance.nacl_owner = request.user
                instance.save()
            return redirect('cusInf_SG')
        else :
            form = forms.nacl4()
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
    infra_name = cs[number-1].infrastructure_name
    sg_number = cs[number-1].infrastructure_sg
    if str(sg_number) == "1":
        if request.method == 'POST':
            form = forms.sg(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.sg_name = str(request.user) + "SG1"
                instance.sg_infra = infra_name
                instance.sg_owner = request.user
                instance.save()
            return redirect('cusInf_Pub_Instance')
        else :
            form = forms.sg()
            context = {
                "form":form,
                "sg" : sg,
            }
            return render(request, "cusInf_SG.html", context)
    if str(sg_number) == "2":
        if request.method == 'POST':
            form = forms.sg2(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.sg_name = str(request.user) + "SG2"
                instance.sg_infra = infra_name
                instance.sg_owner = request.user
                instance.save()
            return redirect('cusInf_Pub_Instance')
        else :
            form = forms.sg2()
            context = {
                "form":form,
                "sg" : sg,
            }
            return render(request, "cusInf_SG.html", context)
    if str(sg_number) == "3":
        if request.method == 'POST':
            form = forms.sg3(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.sg_name = str(request.user) + "SG3"
                instance.sg_infra = infra_name
                instance.sg_owner = request.user
                instance.save()
            return redirect('cusInf_Pub_Instance')
        else :
            form = forms.sg3()
            context = {
                "form":form,
                "sg" : sg,
            }
            return render(request, "cusInf_SG.html", context)
    if str(sg_number) == "4":
        if request.method == 'POST':
            form = forms.sg4(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.sg_name = str(request.user) + "SG3"
                instance.sg_infra = infra_name
                instance.sg_owner = request.user
                instance.save()
            return redirect('cusInf_Pub_Instance')
        else :
            form = forms.sg4()
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
    infra_name = cs[number-1].infrastructure_name
    inst_number = cs[number-1].infrastructure_pubinst
    if str(inst_number) == "1":
        if request.method == 'POST':
            form = forms.instance(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.inst_infra = infra_name
                instance.inst_owner = request.user
                instance.save()
                return redirect('cusInf_Resume')
        else :
            form = forms.instance2()
            context = {
                "form":form,
                "inst" : inst,
            }
        return render(request, "cusInf_Pub_Instance.html", context)
    if str(inst_number) == "2":
        if request.method == 'POST':
            form = forms.instance2(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.inst_infra = infra_name
                instance.inst_owner = request.user
                instance.save()
                return redirect('cusInf_Resume')
        else :
            form = forms.instance2()
            context = {
                "form":form,
                "inst" : inst,
            }
        return render(request, "cusInf_Pub_Instance.html", context)
    if str(inst_number) == "3":
        if request.method == 'POST':
            form = forms.instance3(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.inst_infra = infra_name
                instance.inst_owner = request.user
                instance.save()
                return redirect('cusInf_Resume')
        else :
            form = forms.instance3()
            context = {
                "form":form,
                "inst" : inst,
            }
        return render(request, "cusInf_Pub_Instance.html", context)
    if str(inst_number) == "4":
        if request.method == 'POST':
            form = forms.instance4(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.inst_infra = infra_name
                instance.inst_owner = request.user
                instance.save()
                return redirect('cusInf_Resume')
        else :
            form = forms.instance4()
            context = {
                "form":form,
                "inst" : inst,
            }
        return render(request, "cusInf_Pub_Instance.html", context)
#########################################################
@login_required
def cusInf_Resume(request):
    naclInProt1=""
    naclOutProt1=""
    naclInProt2=""
    naclOutProt2=""
    naclInProt3=""
    naclOutProt3=""
    naclInProt4=""
    naclOutProt4=""
    sgInProt1=""
    sgOutProt1=""
    sgInProt2=""
    sgOutProt2=""
    sgInProt3=""
    sgOutProt3=""
    sgInProt4=""
    sgOutProt4=""

    cs = CustomStack.objects.all()
    number = cs.count()
    infra_name = cs[number-1].infrastructure_name
    nacl_number = cs[number-1].infrastructure_nacl
    sg_number = cs[number-1].infrastructure_sg
    inst_number = cs[number-1].infrastructure_pubinst
    nacl = NACL.objects.all()
    nacl2 = NACL2.objects.all()
    nacl3 = NACL3.objects.all()
    nacl4 = NACL4.objects.all()
    number1 = nacl.count()
    number12 = nacl2.count()
    number13 = nacl3.count()
    number14 = nacl4.count()
    if str(nacl_number) == "1" :
        naclInProt1 = nacl[number1-1].nacl_in_prot
        naclOutProt1 = nacl[number1-1].nacl_out_prot
    elif str(nacl_number) == "2" :
        naclInProt1 = nacl2[number12-1].nacl_in_prot
        naclOutProt1 = nacl2[number12-1].nacl_out_prot
        naclInProt2 = nacl2[number12-1].nacl_in_prot2
        naclOutProt2 = nacl2[number12-1].nacl_out_prot2
    elif str(nacl_number) == "3" :
        naclInProt1 = nacl3[number13-1].nacl_in_prot
        naclOutProt1 = nacl3[number13-1].nacl_out_prot
        naclInProt2 = nacl3[number13-1].nacl_in_prot2
        naclOutProt2 = nacl3[number13-1].nacl_out_prot2
        naclInProt3 = nacl3[number13-1].nacl_in_prot3
        naclOutProt3 = nacl3[number13-1].nacl_out_prot3
    elif str(nacl_number) == "4" :
        naclInProt1 = nacl4[number14-1].nacl_in_prot
        naclOutProt1 = nacl4[number14-1].nacl_out_prot
        naclInProt2 = nacl4[number14-1].nacl_in_prot2
        naclOutProt2 = nacl4[number14-1].nacl_out_prot2
        naclInProt3 = nacl4[number14-1].nacl_in_prot3
        naclOutProt3 = nacl4[number14-1].nacl_out_prot3
        naclInProt4 = nacl4[number14-1].nacl_in_prot4
        naclOutProt4 = nacl4[number14-1].nacl_out_prot4
    else :
        print "false"
    sg = SG.objects.all()
    number2 = sg.count()
    sg2 = SG2.objects.all()
    number22 = sg2.count()
    sg3 = SG3.objects.all()
    number23 = sg3.count()
    sg4 = SG4.objects.all()
    number24 = sg4.count()
    if str(sg_number) == "1" :
        sgInProt1 = sg[number2-1].sg_in_prot
        sgOutProt1 = sg[number2-1].sg_out_prot
    elif str(sg_number) == "2" :
        sgInProt1 = sg2[number22-1].sg_in_prot
        sgOutProt1 = sg2[number22-1].sg_out_prot
        sgInProt2 = sg2[number22-1].sg_in_prot2
        sgOutProt2 = sg2[number22-1].sg_out_prot2
    elif str(sg_number) == "3" :
        sgInProt1 = sg3[number23-1].sg_in_prot
        sgOutProt1 = sg3[number23-1].sg_out_prot
        sgInProt2 = sg3[number23-1].sg_in_prot2
        sgOutProt2 = sg3[number23-1].sg_out_prot2
        sgInProt3 = sg3[number23-1].sg_in_prot3
        sgOutProt3 = sg3[number23-1].sg_out_prot3
    elif str(sg_number) == "4" :
        sgInProt1 = sg4[number24-1].sg_in_prot
        sgOutProt1 = sg4[number24-1].sg_out_prot
        sgInProt2 = sg4[number24-1].sg_in_prot2
        sgOutProt2 = sg4[number24-1].sg_out_prot2
        sgInProt3 = sg4[number24-1].sg_in_prot3
        sgOutProt3 = sg4[number24-1].sg_out_prot3
        sgInProt4 = sg4[number24-1].sg_in_prot4
        sgOutProt4 = sg4[number24-1].sg_out_prot4
    inst = Instance.objects.all()
    number3 = inst.count()
    inst2 = Instance2.objects.all()
    number32 = inst2.count()
    inst3 = Instance3.objects.all()
    number33 = inst3.count()
    inst4 = Instance4.objects.all()
    number34 = inst4.count()
    if str(inst_number) == "1" :
        instAmi1 = inst[number3-1].ami_type
        instType1 = inst[number3-1].instance_type
        context = {
            "infra_name":infra_name,
            "nacl_number":nacl_number,
            "inst_number":inst_number,
            "sg_number":sg_number,
            "naclInProt1":naclInProt1,
            "naclOutProt1":naclOutProt1,
            "sgInProt1":sgInProt1,
            "sgOutProt1":sgOutProt1,
            "instType1":instType1,
            "instAmi1":instAmi1,
        }
        return render(request, "cusInf_Resume.html", context)
    elif str(inst_number) == "2" :
        instAmi1 = inst2[number32-1].ami_type
        instType1 = inst2[number32-1].instance_type
        instAmi2 = inst2[number32-1].ami_type2
        instType2 = inst2[number32-1].instance_type2
        context = {
            "infra_name":infra_name,
            "nacl_number":nacl_number,
            "inst_number":inst_number,
            "sg_number":sg_number,
            "naclInProt1":naclInProt1,
            "naclOutProt1":naclOutProt1,
            "naclInProt2":naclInProt2,
            "naclOutProt2":naclOutProt2,
            "sgInProt1":sgInProt1,
            "sgOutProt1":sgOutProt1,
            "sgInProt2":sgInProt2,
            "sgOutProt2":sgOutProt2,
            "instAmi1":instAmi1,
            "instType1":instType1,
            "instAmi2":instAmi2,
            "instType2":instType2,
            }
        return render(request, "cusInf_Resume.html", context)
    elif str(inst_number) == "3" :
        instAmi1 = inst3[number33-1].ami_type
        instType1 = inst3[number33-1].instance_type
        instAmi2 = inst3[number33-1].ami_type2
        instType2 = inst3[number33-1].instance_type2
        instAmi3 = inst3[number33-1].ami_type3
        instType3 = inst3[number33-1].instance_type3
        context = {
            "infra_name":infra_name,
            "nacl_number":nacl_number,
            "inst_number":inst_number,
            "sg_number":sg_number,
            "naclInProt1":naclInProt1,
            "naclOutProt1":naclOutProt1,
            "naclInProt2":naclInProt2,
            "naclOutProt2":naclOutProt2,
            "naclInProt3":naclInProt3,
            "naclOutProt3":naclOutProt3,
            "sgInProt1":sgInProt1,
            "sgOutProt1":sgOutProt1,
            "sgInProt2":sgInProt2,
            "sgOutProt2":sgOutProt2,
            "sgInProt3":sgInProt3,
            "sgOutProt3":sgOutProt3,
            "instAmi1":instAmi1,
            "instType1":instType1,
            "instAmi2":instAmi2,
            "instType2":instType2,
            "instAmi3":instAmi3,
            "instType3":instType3,
            }
        return render(request, "cusInf_Resume.html", context)
    elif str(inst_number) == "4" :
        instAmi1 = inst4[number34-1].ami_type
        instType1 = inst4[number34-1].instance_type
        instAmi2 = inst4[number34-1].ami_type2
        instType2 = inst4[number34-1].instance_type2
        instAmi3 = inst4[number34-1].ami_type3
        instType3 = inst4[number34-1].instance_type3
        instAmi4 = inst4[number34-1].ami_type4
        instType4 = inst4[number34-1].instance_type4
        context = {
            "infra_name":infra_name,
            "nacl_number":nacl_number,
            "inst_number":inst_number,
            "sg_number":sg_number,
            "naclInProt1":naclInProt1,
            "naclOutProt1":naclOutProt1,
            "naclInProt2":naclInProt2,
            "naclOutProt2":naclOutProt2,
            "naclInProt3":naclInProt3,
            "naclOutProt3":naclOutProt3,
            "naclInProt4":naclInProt4,
            "naclOutProt4":naclOutProt4,
            "sgInProt1":sgInProt1,
            "sgOutProt1":sgOutProt1,
            "sgInProt2":sgInProt2,
            "sgOutProt2":sgOutProt2,
            "sgInProt3":sgInProt3,
            "sgOutProt3":sgOutProt3,
            "sgInProt4":sgInProt4,
            "sgOutProt4":sgOutProt4,
            "instAmi1":instAmi1,
            "instType1":instType1,
            "instAmi2":instAmi2,
            "instType2":instType2,
            "instAmi3":instAmi3,
            "instType3":instType3,
            "instAmi4":instAmi4,
            "instType4":instType4,
            }
        return render(request, "cusInf_Resume.html", context)
    return render(request, "cusInf_Resume.html", {})
#########################################################
@login_required
def cusInf_Create(request):
    sgInProt1=""
    sgOutProt1=""
    sgInProt2=""
    sgOutProt2=""
    sgInProt3=""
    sgOutProt3=""
    sgInProt4=""
    sgOutProt4=""
    instAmi1=""
    cs = CustomStack.objects.all()
    number = cs.count()
    infra_name = cs[number-1].infrastructure_name
    nacl_number = cs[number-1].infrastructure_nacl
    sg_number = cs[number-1].infrastructure_sg
    inst_number = cs[number-1].infrastructure_pubinst
    nacl = NACL.objects.all()
    number1 = nacl.count()
    nacl2 = NACL2.objects.all()
    number12 = nacl2.count()
    nacl3 = NACL3.objects.all()
    number13 = nacl3.count()
    nacl4 = NACL4.objects.all()
    number14 = nacl4.count()
    if str(nacl_number) == "1" :
        naclInProt1 = nacl[number1-1].nacl_in_prot
        naclOutProt1 = nacl[number1-1].nacl_out_prot
    elif str(nacl_number) == "2" :
        naclInProt1 = nacl2[number12-1].nacl_in_prot
        naclOutProt1 = nacl2[number12-1].nacl_out_prot
        naclInProt2 = nacl2[number12-1].nacl_in_prot2
        naclOutProt2 = nacl2[number12-1].nacl_out_prot2
    elif str(nacl_number) == "3" :
        naclInProt1 = nacl3[number13-1].nacl_in_prot
        naclOutProt1 = nacl3[number13-1].nacl_out_prot
        naclInProt2 = nacl3[number13-1].nacl_in_prot2
        naclOutProt2 = nacl3[number13-1].nacl_out_prot2
        naclInProt3 = nacl3[number13-1].nacl_in_prot3
        naclOutProt3 = nacl3[number13-1].nacl_out_prot3
    elif str(nacl_number) == "4" :
        naclInProt1 = nacl4[number14-1].nacl_in_prot
        naclOutProt1 = nacl4[number14-1].nacl_out_prot
        naclInProt2 = nacl4[number14-1].nacl_in_prot2
        naclOutProt2 = nacl4[number14-1].nacl_out_prot2
        naclInProt3 = nacl4[number14-1].nacl_in_prot3
        naclOutProt3 = nacl4[number14-1].nacl_out_prot3
        naclInProt4 = nacl4[number14-1].nacl_in_prot4
        naclOutProt4 = nacl4[number14-1].nacl_out_prot4
    sg = SG.objects.all()
    number2 = sg.count()
    sg2 = SG2.objects.all()
    number22 = sg2.count()
    sg3 = SG3.objects.all()
    number23 = sg3.count()
    sg4 = SG4.objects.all()
    number24 = sg4.count()
    if str(sg_number) == "1" :
        sgInProt1 = sg[number2-1].sg_in_prot
        sgOutProt1 = sg[number2-1].sg_out_prot
    elif str(sg_number) == "2" :
        sgInProt1 = sg2[number22-1].sg_in_prot
        sgOutProt1 = sg2[number22-1].sg_out_prot
        sgInProt2 = sg2[number22-1].sg_in_prot2
        sgOutProt2 = sg2[number22-1].sg_out_prot2
    elif str(sg_number) == "3" :
        sgInProt1 = sg3[number23-1].sg_in_prot
        sgOutProt1 = sg3[number23-1].sg_out_prot
        sgInProt2 = sg3[number23-1].sg_in_prot2
        sgOutProt2 = sg3[number23-1].sg_out_prot2
        sgInProt3 = sg3[number23-1].sg_in_prot3
        sgOutProt3 = sg3[number23-1].sg_out_prot3
    elif str(sg_number) == "4" :
        sgInProt1 = sg4[number24-1].sg_in_prot
        sgOutProt1 = sg4[number24-1].sg_out_prot
        sgInProt2 = sg4[number24-1].sg_in_prot2
        sgOutProt2 = sg4[number24-1].sg_out_prot2
        sgInProt3 = sg4[number24-1].sg_in_prot3
        sgOutProt3 = sg4[number24-1].sg_out_prot3
        sgInProt4 = sg4[number24-1].sg_in_prot4
        sgOutProt4 = sg4[number24-1].sg_out_prot4
    inst = Instance.objects.all()
    number3 = inst.count()
    inst2 = Instance2.objects.all()
    number32 = inst2.count()
    inst3 = Instance3.objects.all()
    number33 = inst3.count()
    inst4 = Instance4.objects.all()
    number34 = inst4.count()
    if str(inst_number) == "1" :
        instAmi1 = inst[number3-1].ami_type
        instType1 = inst[number3-1].instance_type
    elif str(inst_number) == "2" :
         instAmi1 = inst2[number32-1].ami_type
         instType1 = inst2[number32-1].instance_type
         instAmi2 = inst2[number32-1].ami_type2
         instType2 = inst2[number32-1].instance_type2
    elif str(inst_number) == "3" :
         instAmi1 = inst3[number33-1].ami_type
         instType1 = inst3[number33-1].instance_type
         instAmi2 = inst3[number33-1].ami_type2
         instType2 = inst3[number33-1].instance_type2
         instAmi3 = inst3[number33-1].ami_type3
         instType3 = inst3[number33-1].instance_type3
    elif str(inst_number) == "4" :
         instAmi1 = inst4[number34-1].ami_type
         instType1 = inst4[number34-1].instance_type
         instAmi2 = inst4[number34-1].ami_type2
         instType2 = inst4[number34-1].instance_type2
         instAmi3 = inst4[number34-1].ami_type3
         instType3 = inst4[number34-1].instance_type3
         instAmi4 = inst4[number34-1].ami_type4
         instType4 = inst4[number34-1].instance_type4
    ec2 = boto3.resource('ec2')
    # create VPC
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    # we can assign a name to vpc, or any resource, by using tag
    vpc.create_tags(Tags=[{"Key": "Name", "Value": "CustomVPC"}])
    vpc.wait_until_available()
    print(vpc.id)
    # create then attach internet gateway
    ig = ec2.create_internet_gateway()
    vpc.attach_internet_gateway(InternetGatewayId=ig.id)
    print(ig.id)
    # create a route table and a public route
    route_table = vpc.create_route_table()
    route = route_table.create_route(
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=ig.id
    )
    print(route_table.id)
    # create subnet
    subnet = ec2.create_subnet(CidrBlock='10.0.0.0/24', VpcId=vpc.id)
    print(subnet.id)
    # associate the route table with the subnet
    route_table.associate_with_subnet(SubnetId=subnet.id)
    if str(inst_number) == "1" :
        # Create sec group
        if str(sg_number) == "1" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
    if str(inst_number) == "2" :
        if str(sg_number) == "1" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)# Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
        if str(sg_number) == "2" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
    if str(inst_number) == "3" :
        if str(sg_number) == "1" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)# Create instance
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
        if str(sg_number) == "2" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
        if str(sg_number) == "3" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            sec_group3 = ec2.create_security_group(GroupName='CustomSG3', Description='Custom security group', VpcId=vpc.id)
            if sgInProt3== "ICMP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt3 == "ICMP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "ALL":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt3 == "ALL":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "SSH":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt3 == "SSH":
                sec_group3.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt3 == "HTTP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt3 == "HTTP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group3.id)

            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
    if str(inst_number) == "4" :
        if sg_number == "1" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi4 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
        if sg_number == "2" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            if instAmi4 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
        if sg_number == "3" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            sec_group3 = ec2.create_security_group(GroupName='CustomSG3', Description='Custom security group', VpcId=vpc.id)
            if sgInProt3== "ICMP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt3 == "ICMP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "ALL":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt3 == "ALL":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "SSH":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt3 == "SSH":
                sec_group3.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt3 == "HTTP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt3 == "HTTP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group3.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            if instAmi4 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
        if sg_number == "4" :
            sec_group = ec2.create_security_group(GroupName='CustomSG', Description='Custom security group', VpcId=vpc.id)
            if sgInProt1 == "ICMP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt1 == "ICMP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "ALL":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt1 == "ALL":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt1 == "SSH":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt1 == "SSH":
                sec_group.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt1 == "HTTP":
                sec_group.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt1 == "HTTP":
                sec_group.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group.id)
            sec_group2 = ec2.create_security_group(GroupName='CustomSG2', Description='Custom security group', VpcId=vpc.id)
            if sgInProt2 == "ICMP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt2 == "ICMP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "ALL":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt2 == "ALL":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt2 == "SSH":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt2 == "SSH":
                sec_group2.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt2 == "HTTP":
                sec_group2.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt2 == "HTTP":
                sec_group2.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group2.id)
            sec_group3 = ec2.create_security_group(GroupName='CustomSG3', Description='Custom security group', VpcId=vpc.id)
            if sgInProt3== "ICMP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt3 == "ICMP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "ALL":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt3 == "ALL":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt3 == "SSH":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt3 == "SSH":
                sec_group3.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt3 == "HTTP":
                sec_group3.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt3 == "HTTP":
                sec_group3.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group3.id)
            sec_group4 = ec2.create_security_group(GroupName='CustomSG4', Description='Custom security group', VpcId=vpc.id)
            if sgInProt4== "ICMP":
                sec_group4.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="ICMP",
                    FromPort=-1,
                    ToPort=-1
                )
            elif sgOutProt4 == "ICMP":
                sec_group4.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "ICMP",
                        'FromPort': -1,
                        'ToPort': -1,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt4 == "ALL":
                sec_group4.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=0,
                    ToPort=65535
                )
            elif sgOutProt4 == "ALL":
                sec_group4.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 0,
                        'ToPort': 65535,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            elif sgInProt4 == "SSH":
                sec_group4.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort= 22,
                    ToPort= 22
                )
            elif sgOutProt4 == "SSH":
                sec_group4.authorize_egress(
                    IpPermissions=[
                        {
                            'IpProtocol': 'TCP',
                            'FromPort': 22,
                            'ToPort': 22,
                            'IpRanges': [
                                {'CidrIp': '0.0.0.0/0'}
                            ]
                        }
                    ]
                )
            elif sgInProt4 == "HTTP":
                sec_group4.authorize_ingress(
                    CidrIp='0.0.0.0/0',
                    IpProtocol="TCP",
                    FromPort=80,
                    ToPort=80
                )
            elif sgOutProt4 == "HTTP":
                sec_group4.authorize_egress(
                    IpPermissions=[{
                        'IpProtocol': "TCP",
                        'FromPort': 80,
                        'ToPort': 80,
                        'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
                    }]
                )
            print(sec_group4.id)
            # Create instance
            if instAmi1 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            elif instAmi1 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance1'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
                instances[0].wait_until_running()
            if instAmi2 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            elif instAmi2 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance2'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group2.group_id]}])
                instances[0].wait_until_running()
            if instAmi3 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            elif instAmi3 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance3'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group3.group_id]}])
                instances[0].wait_until_running()
            if instAmi4 == "Amazon AMI":
                instances = ec2.create_instances(
                    ImageId='ami-058f46b781900723c',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group4.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "RedHat":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group4.group_id]}])
                instances[0].wait_until_running()
            elif instAmi4 == "Ubuntu Server":
                instances = ec2.create_instances(
                    ImageId='ami-7c1bfd1b',KeyName='newkp', InstanceType=instType1, MaxCount=1, MinCount=1,
                    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name', 'Value':'CustInstance4'},]},],
                    NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group4.group_id]}])
                instances[0].wait_until_running()
    print(instances[0].id)

    return render(request,"user.html",{})
#########################################################
def cusInf_Delete(request):
    cs = CustomStack.objects.all()
    number = cs.count()
    owner = cs[number-1].infrastructure_owner
    infra_name = cs[number-1].infrastructure_name
    inst_number = cs[number-1].infrastructure_pubinst
    sg_number = cs[number-1].infrastructure_sg

    ip=[]
    ip_2=[]
    ip_3=[]
    ip_4=[]
    id=[]
    sgid=[]
    sgid_2=[]
    sgid_3=[]
    sgid_4=[]
    subid=[]
    rtid = []
    rtid2 = []
    igid=[]
    ec2 = boto3.resource('ec2')
    client = boto3.client('ec2')
    if str(inst_number) == "1":
        response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
        for each in response['Reservations']:
            ipadd = each['Instances'][0]['InstanceId']
            ip.append(ipadd)
            vpcid = each['Instances'][0]['VpcId']
            id.append(vpcid)
            sg = each['Instances'][0]['SecurityGroups']
            sg_id = sg[0]['GroupId']
            sgid.append(sg_id)
            subnet = each['Instances'][0]['SubnetId']
            subid.append(subnet)
        idsg = sgid[0]
        idvpc = id[0]
        instip = ip[0]
        idsub = subid[0]
        response2 = client.describe_vpcs(VpcIds=[idvpc,],)
        response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
        for each in response3['RouteTables']:
            if each['Associations'][0]['Main'] == False :
                rt = each['RouteTableId']
                rtid.append(rt)
            if each['Associations'][0]['Main'] == True :
                rt2 = each['RouteTableId']
                rtid2.append(rt2)
        idrt = rtid[0]
        idrt2 = rtid2[0]
        response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
        for each in response4['InternetGateways'] :
            ig = each['InternetGatewayId']
            igid.append(ig)
        idig=igid[0]
        instance = ec2.Instance(instip)
        instance.terminate()
        print "wait untill your instance terminates"
        instance.wait_until_terminated()
        print 'your instance is terminated now'
        client.delete_security_group(GroupId=idsg)
        print "success sg"
        client.delete_subnet(SubnetId=idsub)
        print "success subnet"
        client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
        print "success route"
        client.delete_route_table(RouteTableId=idrt)
        print "success route table1"
        # client.delete_route_table(RouteTableId=idrt2)
        # print "success route table2"
        client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
        print "success internet gateway"
        client.delete_vpc(VpcId=idvpc)
        print "success vpc"
        client.delete_internet_gateway(InternetGatewayId=idig)
        print "success internet gateway"
        custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
        custinst.delete()
    if str(inst_number) == "2":
        if str(sg_number) == "1":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)

            idsg = sgid[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "2":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg 2"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
    if str(inst_number) == "3":
        if str(sg_number) == "1":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)

            idsg = sgid[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'instance 3 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "2":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill your instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'your instance 3 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg 2"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "3":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)
                sg_3 = each['Instances'][0]['SecurityGroups']
                sg_id_3 = sg_3[0]['GroupId']
                sgid_3.append(sg_id_3)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idsg_3 = sgid_3[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill your instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'your instance 3 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg 2"
            client.delete_security_group(GroupId=idsg_3)
            print "success sg 3"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
    if str(inst_number) == "4":
        if str(sg_number) == "1":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_4 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance4',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)
            for each in response_4['Reservations']:
                ipadd_4 = each['Instances'][0]['InstanceId']
                ip_4.append(ipadd_4)

            idsg = sgid[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            instip_4 = ip_4[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'instance 3 is terminated now'
            instance_4 = ec2.Instance(instip_4)
            instance_4.terminate()
            print "wait untill instance 4 terminates"
            instance_4.wait_until_terminated()
            print 'instance 4 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "2":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_4 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance4',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)
            for each in response_4['Reservations']:
                ipadd_4 = each['Instances'][0]['InstanceId']
                ip_4.append(ipadd_4)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            instip_4 = ip_4[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'instance 3 is terminated now'
            instance_4 = ec2.Instance(instip_4)
            instance_4.terminate()
            print "wait untill instance 4 terminates"
            instance_4.wait_until_terminated()
            print 'instance 4 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg2"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "3":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_4 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance4',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)
                sg_3 = each['Instances'][0]['SecurityGroups']
                sg_id_3 = sg_3[0]['GroupId']
                sgid_3.append(sg_id_3)
            for each in response_4['Reservations']:
                ipadd_4 = each['Instances'][0]['InstanceId']
                ip_4.append(ipadd_4)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idsg_3 = sgid_3[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            instip_4 = ip_4[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'instance 3 is terminated now'
            instance_4 = ec2.Instance(instip_4)
            instance_4.terminate()
            print "wait untill instance 4 terminates"
            instance_4.wait_until_terminated()
            print 'instance 4 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg2"
            client.delete_security_group(GroupId=idsg_3)
            print "success sg3"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
        if str(sg_number) == "4":
            response = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance1',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_2 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance2',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_3 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance3',]},{'Name':'instance-state-name','Values':['running',]},],)
            response_4 = client.describe_instances(Filters=[{'Name': 'tag:Name','Values': ['CustInstance4',]},{'Name':'instance-state-name','Values':['running',]},],)
            for each in response['Reservations']:
                ipadd = each['Instances'][0]['InstanceId']
                ip.append(ipadd)
                vpcid = each['Instances'][0]['VpcId']
                id.append(vpcid)
                sg = each['Instances'][0]['SecurityGroups']
                sg_id = sg[0]['GroupId']
                sgid.append(sg_id)
                subnet = each['Instances'][0]['SubnetId']
                subid.append(subnet)
            for each in response_2['Reservations']:
                ipadd_2 = each['Instances'][0]['InstanceId']
                ip_2.append(ipadd_2)
                sg_2 = each['Instances'][0]['SecurityGroups']
                sg_id_2 = sg_2[0]['GroupId']
                sgid_2.append(sg_id_2)
            for each in response_3['Reservations']:
                ipadd_3 = each['Instances'][0]['InstanceId']
                ip_3.append(ipadd_3)
                sg_3 = each['Instances'][0]['SecurityGroups']
                sg_id_3 = sg_3[0]['GroupId']
                sgid_3.append(sg_id_3)
            for each in response_4['Reservations']:
                ipadd_4 = each['Instances'][0]['InstanceId']
                ip_4.append(ipadd_4)
                sg_4 = each['Instances'][0]['SecurityGroups']
                sg_id_4 = sg_4[0]['GroupId']
                sgid_4.append(sg_id_4)

            idsg = sgid[0]
            idsg_2 = sgid_2[0]
            idsg_3 = sgid_3[0]
            idsg_4 = sgid_4[0]
            idvpc = id[0]
            instip = ip[0]
            instip_2 = ip_2[0]
            instip_3 = ip_3[0]
            instip_4 = ip_4[0]
            idsub = subid[0]
            response2 = client.describe_vpcs(VpcIds=[idvpc,],)
            response3 = client.describe_route_tables(Filters=[{'Name': 'vpc-id','Values': [idvpc,]},],)
            for each in response3['RouteTables']:
                if each['Associations'][0]['Main'] == False :
                    rt = each['RouteTableId']
                    rtid.append(rt)
                if each['Associations'][0]['Main'] == True :
                    rt2 = each['RouteTableId']
                    rtid2.append(rt2)
            idrt = rtid[0]
            idrt2 = rtid2[0]
            response4= client.describe_internet_gateways(Filters=[{'Name': 'attachment.vpc-id','Values': [idvpc,]},],)
            for each in response4['InternetGateways'] :
                ig = each['InternetGatewayId']
                igid.append(ig)
            idig=igid[0]
            instance = ec2.Instance(instip)
            instance.terminate()
            print "wait untill your instance terminates"
            instance.wait_until_terminated()
            print 'your instance is terminated now'
            instance_2 = ec2.Instance(instip_2)
            instance_2.terminate()
            print "wait untill your instance 2 terminates"
            instance_2.wait_until_terminated()
            print 'your instance 2 is terminated now'
            instance_3 = ec2.Instance(instip_3)
            instance_3.terminate()
            print "wait untill instance 3 terminates"
            instance_3.wait_until_terminated()
            print 'instance 3 is terminated now'
            instance_4 = ec2.Instance(instip_4)
            instance_4.terminate()
            print "wait untill instance 4 terminates"
            instance_4.wait_until_terminated()
            print 'instance 4 is terminated now'
            client.delete_security_group(GroupId=idsg)
            print "success sg"
            client.delete_security_group(GroupId=idsg_2)
            print "success sg2"
            client.delete_security_group(GroupId=idsg_3)
            print "success sg3"
            client.delete_security_group(GroupId=idsg_4)
            print "success sg4"
            client.delete_subnet(SubnetId=idsub)
            print "success subnet"
            client.delete_route(RouteTableId=idrt,DestinationCidrBlock='0.0.0.0/0',)
            print "success route"
            client.delete_route_table(RouteTableId=idrt)
            print "success route table1"
            # client.delete_route_table(RouteTableId=idrt2)
            # print "success route table2"
            client.detach_internet_gateway(InternetGatewayId=idig,VpcId=idvpc)
            print "success internet gateway"
            client.delete_vpc(VpcId=idvpc)
            print "success vpc"
            client.delete_internet_gateway(InternetGatewayId=idig)
            print "success internet gateway"
            custinst = CustomStack.objects.get(infrastructure_name = infra_name, infrastructure_owner = owner )
            custinst.delete()
    return render(request, "user.html", {})
#########################################################
##########################
##########################
########################################################
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

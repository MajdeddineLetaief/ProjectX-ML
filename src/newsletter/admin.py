# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import SignUp, DefaultStack, CustomStack, Nacl
from .forms import SignUpForm
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    ##########################################################
    #this is how it was before creating SignUpForm in forms.py
    # class Meta:
    #     model = SignUp
    
admin.site.register(Nacl)
admin.site.register(DefaultStack)
admin.site.register(CustomStack)

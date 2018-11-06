# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import SignUp, DefaultStack, CustomStack, NACL,NACL2,NACL3,NACL4, SG,SG2,SG3,SG4, Instance,Instance2,Instance3,Instance4
from .forms import SignUpForm
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    ##########################################################
    #this is how it was before creating SignUpForm in forms.py
    # class Meta:
    #     model = SignUp

admin.site.register(Instance)
admin.site.register(Instance2)
admin.site.register(Instance3)
admin.site.register(Instance4)
admin.site.register(SG)
admin.site.register(SG2)
admin.site.register(SG3)
admin.site.register(SG4)
admin.site.register(NACL)
admin.site.register(NACL2)
admin.site.register(NACL3)
admin.site.register(NACL4)
admin.site.register(DefaultStack)
admin.site.register(CustomStack)

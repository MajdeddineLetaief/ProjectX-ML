# from registration.forms import RegistrationForm
from django import forms
from .models import SignUp, DefaultStack, CustomStack, Nacl, SG
from django.forms.widgets import CheckboxSelectMultiple

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
    ############### Validation code examples ##############################################
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split('@')
    #     domain, extension = provider.split('.')
    #     if not domain == 'agyla':
    #         raise forms.ValidationError('Please make sure that you use an AGYLA email !')
    #     if not extension == '.com':
    #         raise forms.ValidationError('Please make sure that you use .COM extension !')
    #     return email
    #
    # def clean_full_name(self):
    #     full_name = self.cleaned_data.get('full_name')
    #     #validation code
    #     return full_name


class createInfra(forms.ModelForm):
    class Meta:
        model = DefaultStack
        fields = ['infrastructure_name']

class customInfra(forms.ModelForm):
    class Meta:
        model = CustomStack
        fields = ['infrastructure_name',
                  'infrastructure_pubsub',
                  'infrastructure_prvsub',
                  'infrastructure_nacl',
                  'infrastructure_sg',
                  'infrastructure_pubinst',
                  'infrastructure_prvinst']


class Nacl(forms.ModelForm):
    class Meta:
        model = Nacl
        fields = ['nacl_name', 'nacl_src_ip','type']

class SG(forms.ModelForm):
    class Meta:
        model = SG
        fields = ['sg_name', 'sg_src_ip','type']

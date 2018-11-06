# from registration.forms import RegistrationForm
from django import forms
from .models import SignUp, DefaultStack, CustomStack, NACL,NACL2,NACL3,NACL4, SG,SG2,SG3,SG4, Instance,Instance2,Instance3,Instance4
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
                  # 'infrastructure_pubsub',
                  # 'infrastructure_prvsub',
                  'infrastructure_nacl',
                  'infrastructure_sg',
                  'infrastructure_pubinst',]

class nacl(forms.ModelForm):
    class Meta:
        model = NACL
        fields = [
                  'nacl_in_prot',
                  'nacl_out_prot']

class nacl2(forms.ModelForm):
    class Meta:
        model = NACL2
        fields = ['nacl_in_prot','nacl_out_prot','nacl_in_prot2','nacl_out_prot2']

class nacl3(forms.ModelForm):
    class Meta:
        model = NACL3
        fields = ['nacl_in_prot','nacl_out_prot','nacl_in_prot2','nacl_out_prot2','nacl_in_prot3','nacl_out_prot3']

class nacl4(forms.ModelForm):
    class Meta:
        model = NACL4
        fields = ['nacl_in_prot','nacl_out_prot','nacl_in_prot2','nacl_out_prot2','nacl_in_prot3','nacl_out_prot3','nacl_in_prot4','nacl_out_prot4']

class sg(forms.ModelForm):
    class Meta:
        model = SG
        fields = ['sg_in_prot','sg_out_prot']

class sg2(forms.ModelForm):
    class Meta:
        model = SG2
        fields = ['sg_in_prot','sg_out_prot','sg_in_prot2','sg_out_prot2']

class sg3(forms.ModelForm):
    class Meta:
        model = SG3
        fields = ['sg_in_prot','sg_out_prot','sg_in_prot2','sg_out_prot2','sg_in_prot3','sg_out_prot3']

class sg4(forms.ModelForm):
    class Meta:
        model = SG4
        fields = ['sg_in_prot','sg_out_prot','sg_in_prot2','sg_out_prot2','sg_in_prot3','sg_out_prot3','sg_in_prot4','sg_out_prot4']

class instance(forms.ModelForm):
    class Meta:
        model = Instance
        fields = ['ami_type', 'instance_type']

class instance2(forms.ModelForm):
    class Meta:
        model = Instance2
        fields = ['ami_type', 'instance_type','ami_type2', 'instance_type2']

class instance3(forms.ModelForm):
    class Meta:
        model = Instance3
        fields = ['ami_type', 'instance_type','ami_type2', 'instance_type2','ami_type3', 'instance_type3']

class instance4(forms.ModelForm):
    class Meta:
        model = Instance4
        fields = ['ami_type', 'instance_type','ami_type2', 'instance_type2','ami_type3', 'instance_type3','ami_type4', 'instance_type4']

from django import forms
from checkout.models import BillingDetail

# class BillingDetailForm(forms.Form):
#     first_name = forms.CharField(max_length=25)
#     last_name = forms.CharField(max_length=25)
#     company_name = forms.CharField(max_length=75, required=False)
#     country = forms.ChoiceField(choices=(('Nepal', 'Nepal'),))
#     district = forms.CharField(max_length=25)
#     city = forms.CharField(max_length=25)
#     street = forms.CharField(max_length=25, required=False)
#     zip_code = forms.CharField(max_length=10)
#     phone = forms.CharField(max_length=15)
#     email = forms.EmailField()
#     order_notes = forms.CharField(widget=forms.Textarea)

class BillingDetailForm(forms.ModelForm):
    class Meta:
        model = BillingDetail
        fields = ['first_name', 'last_name', 'company_name', 'country', 'district', 'city', 'street', 'zip_code', 'phone', 'email', 'order_notes', 'payment_method']

        PAYMENT_CHOICES = (('Cash on delivery', 'Cash on delivery'),
                            ('Direct bank transfer', 'Direct bank transfer'),
                            ('Cheque payments', 'Cheque payments'),)

        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name *'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name *'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Company Name'}),
            'country' : forms.Select(choices=(('Nepal', 'Nepal'),), attrs={'placeholder':'Country *'}),
            'district' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'District *'}),
            'city' : forms.TextInput(attrs={'class':'form-control arun', 'placeholder':'Town/City *'}),
            'street' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street address'}),

            'zip_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip/Post Code'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone No *'}),
            'email' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address *'}),
            'order_notes' : forms.Textarea(attrs={'class':'form-control arunotes', 'placeholder':'Note about your order'}),

            'payment_method' : forms.Select(choices=PAYMENT_CHOICES)
        }

        # widgets = {
        #     'first_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'last_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'company_name' : forms.TextInput(attrs={'class':'form-control'}),
        #     'country' : forms.Select(choices=(('Nepal', 'Nepal'),), attrs={'class':'form-control'}),
        #     'district' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'District'}),
        #     'city' : forms.TextInput(attrs={'class':'form-control arun', 'placeholder':'City'}),
        #     'street' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Street address'}),
        #
        #     'zip_code' : forms.TextInput(attrs={'class':'form-control'}),
        #     'phone' : forms.TextInput(attrs={'class':'form-control'}),
        #     'email' : forms.TextInput(attrs={'class':'form-control'}),
        #     'order_notes' : forms.Textarea(attrs={'class':'form-control arunotes', 'placeholder':'Note about your order'}),
        #
        #     'payment_method' : forms.RadioSelect(choices=PAYMENT_CHOICES)
        # }

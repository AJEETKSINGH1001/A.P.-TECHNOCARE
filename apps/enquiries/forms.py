
from django import forms

from .models import Enquiry, ContactMessage


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = [
            "name",
            "company_name",
            "phone",
            "email",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your full name",
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company name (optional)",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your phone number",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email address",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "How can we help you?",
            }),
        }


class ProductEnquiryForm(forms.Form):
    customer_name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your full name",
        }),
    )

    company_name = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Company name (optional)",
        }),
    )

    phone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your phone number",
        }),
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Your email address",
        }),
    )

    quantity = forms.DecimalField(
        required=False,
        min_value=0,
        max_digits=12,
        decimal_places=3,
        initial=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "min": "0",
            "step": "0.001",
        }),
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 4,
            "placeholder": "Tell us your requirements",
        }),
    )


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "company_name",
            "email",
            "phone",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your name",
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company name (optional)",
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Your email address",
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your phone number",
            }),
            "subject": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Subject",
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your message",
            }),
        }
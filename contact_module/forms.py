from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوداگی'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع پیام'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'پیغام خود را اینجا بنویسید...'}),
        }

        error_messages = {
            'full_name': {
                'required': 'لطفا نام و نام خانوادگی خود را وارد نمایید',
            },
            'email': {
                'required': 'لطفا ایمیل خود را وارد نمایید'
            },
            'title': {
                'required': 'لطفا موضوع پیام خود را وارد نمایید'
            },
            'message': {
                'required': 'لطفا پیام خود را وارد نمایید'
            }
        }



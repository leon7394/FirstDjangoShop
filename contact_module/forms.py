from django import forms

class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label='نام و نام خانوادگی',
        max_length=300,
        required=True,
        error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد نمایید'}
    )
    email = forms.EmailField(label='ایمیل', required=True, error_messages={'required': 'ایمیل الزامی است'})
    subject = forms.CharField(label='موضوع', required=True, error_messages={'required': 'لطفا موضوع را وارد کنید'})
    messages = forms.CharField(widget=forms.Textarea, label='پیغام شما', required=True, error_messages={'required': 'لطفا پیام خود را وارد کنید'})

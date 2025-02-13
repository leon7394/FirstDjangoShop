from django import forms
from django.core import validators


class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=300, required=True,
        error_messages={
            'required' : 'لطفا نام و نام خانوادگی خود را وارد نمایید',
            'max_length' : 'نام و نام خانوادگی نمیتواند بیش تر از 50 کاراکتر باشد',
        },
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوداگی' })
    )
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        error_messages = {
        'required': 'لطفا ایمیل خود را وارد نمایید'},
        # validators=[validators.validate_email ]
    )

    title = forms.CharField(label='موضوع', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'موضوع پیام'}),
                            error_messages={
            'required': 'لطفا موضوع پیام خود را وارد نمایید'}
                            )

    message = forms.CharField(label='پیغام شما', widget=forms.Textarea(
        attrs={ 'class': 'form-control', 'id' : 'message', 'placeholder': 'پیغام خود را اینجا بنویسید...',}),
                              error_messages={
            'required': 'لطفا پیام خود را وارد نمایید'}
                              )


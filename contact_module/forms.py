from django import forms

class ContactUsForm(forms.Form):
    full_name = forms.CharField(label='نام و نام خانوادگی', max_length=300, required=True, error_messages={
        'required' : 'لطفا نام و نام خانوادگی خود را وارد نمایید'
    })
    email = forms.EmailField(label='ایمیل')
    subject = forms.CharField(label= 'موضوع')
    messages = forms.CharField(widget=forms.Textarea, label='پیغام شما')

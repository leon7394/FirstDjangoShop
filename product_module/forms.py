from django import forms
from product_module.models import ProductComment


class ProductCommentModelForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

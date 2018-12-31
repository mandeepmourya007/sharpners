from django import forms

class postForm(forms.Form):
    title = forms.EmailField(required=True)
    tag = forms.CharField(required=True)
    text = forms.CharField(widget=forms.Textarea)

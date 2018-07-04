from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    bookId = forms.CharField()
    product_name = forms.CharField()

class ContactForm_2(forms.Form):
    email = forms.EmailField(required=True)
    name = forms.CharField(required=True)
    phonenumber= forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


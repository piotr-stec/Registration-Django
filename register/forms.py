from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['child_name', 'child_class', 'parent_name1', 'parent_name2', 'parent_phone_number1',
                  'parent_phone_number2', 'email', 'swietlica', 'payment']
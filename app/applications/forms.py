from django import forms
from django.forms import CheckboxSelectMultiple, NumberInput, Select, TextInput, HiddenInput
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Application


class ApplicationCreateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
        widgets = {
            "carer": HiddenInput(
                attrs={
                    "class": "rounded-pill shadow",
                }
            ),
            "job": HiddenInput(),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Application already exit",
            }
        }

       
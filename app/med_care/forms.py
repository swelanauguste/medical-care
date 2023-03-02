from django import forms
from django.forms import CheckboxSelectMultiple, NumberInput, Select, TextInput

from .models import MedicalCareProfile


class MedicalCareProfileCreateForm(forms.ModelForm):
    class Meta:
        model = MedicalCareProfile
        fields = ["carer", "exp", "qualifications", "skills", "hourly_rate"]
        widgets = {
            "carer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "qualifications": CheckboxSelectMultiple(),
            "skills": CheckboxSelectMultiple(),
            "exp": TextInput(
                attrs={
                    "class": "rounded-pill shadow",
                    "type": "text",
                    "inputmode": "numeric",
                    "pattern": "[0-9]",
                }
            ),
            "hourly_rate": TextInput(
                attrs={
                    "class": "rounded-pill shadow",
                }
            ),
        }
        labels = {
            "carer": "",
        }


class MedicalCareProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = MedicalCareProfile
        fields = "__all__"
        exclude = ["carer", "uid", "slug"]
        widgets = {
            "exp": TextInput(
                attrs={
                    "class": "rounded-pill shadow",
                    "inputmode": "numeric",
                    "type": "text",
                    "pattern": "[0-9]+",
                }
            ),
            "qualifications": CheckboxSelectMultiple(),
            "skills": CheckboxSelectMultiple(),
            "hourly_rate": TextInput(
                attrs={
                    "class": "rounded-pill shadow",
                }
            ),
        }

        labels = {
            "qualifications": "",
            "skills": "",
        }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

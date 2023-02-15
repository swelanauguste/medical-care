from django import forms
from django.forms import CheckboxSelectMultiple, Select, TextInput

from .models import MedicalCareProfile


class MedicalCareProfileCreateForm(forms.ModelForm):
    class Meta:
        model = MedicalCareProfile
        fields = ["carer", "exp", "qualifications", "skills"]
        widgets = {
            "carer": Select(
                attrs={"class": "visually-hidden-focusable"},
            ),
            "exp": TextInput(attrs={"class": "rounded-pill shadow"}),
            "qualifications": CheckboxSelectMultiple(),
            "skills": CheckboxSelectMultiple(),
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
            "exp": TextInput(attrs={"class": "rounded-pill shadow"}),
            "qualifications": CheckboxSelectMultiple(),
            "skills": CheckboxSelectMultiple(),
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

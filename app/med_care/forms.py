from django import forms
from django.forms import CheckboxSelectMultiple, TextInput

from .models import MedicalCareProfile


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

        # labels = {
        #     'gender': 'Sex',
        #     'phone1': '<small class="text-muted">Alt. Phone</small>',
        # }
        # help_texts = {
        #     'name': _('Some useful help text.'),
        # }
        # error_messages = {
        #     'name': {
        #         'max_length': _("This writer's name is too long."),
        #     },
        # }

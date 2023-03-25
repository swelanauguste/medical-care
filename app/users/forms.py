from django import forms
from django.forms import (
    DateInput,
    FileInput,
    ImageField,
    RadioSelect,
    Select,
    Textarea,
    TextInput,
)

from .models import Profile, User

rounded_pill_shadow = "rounded-4"
no_border = "border-0 border-bottom rounded-0"


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["is_buyer", "is_seller"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user", "uid", "slug"]
        widgets = {
            "bio": Textarea(attrs={"cols": 80, "rows": 4, "class": no_border}),
            "dob": DateInput(attrs={"class": no_border, "type": "date"}),
            "first_name": TextInput(attrs={"class": no_border}),
            "last_name": TextInput(attrs={"class": no_border}),
            "middle_name": TextInput(attrs={"class": no_border}),
            "title": Select(attrs={"class": no_border}),
            "address": TextInput(attrs={"class": no_border}),
            "address1": TextInput(attrs={"class": no_border}),
            "postal_code": TextInput(attrs={"class": no_border}),
            "gender": RadioSelect(),
            "location": Select(attrs={"class": no_border}),
            "image": FileInput(attrs={"class": "form-control rounded-4 mb-lg-2"}),
            "phone": TextInput(
                attrs={
                    "class": no_border,
                    "inputmode": "numeric",
                    "type": "text",
                    "pattern": "+[0-9]",
                    "placeholder": "758-489-3909",
                }
            ),
            "phone1": TextInput(
                attrs={
                    "class": no_border,
                    "inputmode": "numeric",
                    "type": "text",
                    "pattern": "+[0-9]",
                    "placeholder": "758-489-3909",
                }
            ),
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

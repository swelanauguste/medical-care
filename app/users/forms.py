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
            "bio": Textarea(attrs={"cols": 80, "rows": 4, "class": "rounded-3"}),
            "dob": DateInput(attrs={"class": rounded_pill_shadow, "type": "date"}),
            "first_name": TextInput(attrs={"class": rounded_pill_shadow}),
            "last_name": TextInput(attrs={"class": rounded_pill_shadow}),
            "middle_name": TextInput(attrs={"class": rounded_pill_shadow}),
            "title": Select(attrs={"class": rounded_pill_shadow}),
            "address": TextInput(attrs={"class": rounded_pill_shadow}),
            "address1": TextInput(attrs={"class": rounded_pill_shadow}),
            "postal_code": TextInput(attrs={"class": rounded_pill_shadow}),
            "gender": RadioSelect(),
            "location": Select(attrs={"class": rounded_pill_shadow}),
            "image": FileInput(attrs={"class": "form-control rounded-4"}),
            "phone": TextInput(
                attrs={
                    "class": rounded_pill_shadow,
                    "inputmode": "numeric",
                    "type": "text",
                    "pattern": "+[0-9]",
                    "placeholder": "758-489-3909",
                }
            ),
            "phone1": TextInput(
                attrs={
                    "class": "rounded-pill",
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

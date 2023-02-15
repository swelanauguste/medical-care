from django import forms
from django.forms import DateInput, RadioSelect, Select, Textarea, TextInput

from .models import Profile, User


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
            "bio": Textarea(attrs={"cols": 80, "rows": 4, "class": "rounded-4 shadow"}),
            "dob": DateInput(attrs={"class": "rounded-3 shadow", "type": "date"}),
            "first_name": TextInput(attrs={"class": "rounded-3 shadow"}),
            "last_name": TextInput(attrs={"class": "rounded-3 shadow"}),
            "middle_name": TextInput(attrs={"class": "rounded-3 shadow"}),
            "gender": RadioSelect(),
            "location": Select(attrs={"class": "rounded-3 shadow"}),
            "phone": TextInput(
                attrs={"class": "rounded-3 shadow", "placeholder": "758-489-3909"}
            ),
            "phone1": TextInput(attrs={"class": "rounded-3 shadow"}),
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

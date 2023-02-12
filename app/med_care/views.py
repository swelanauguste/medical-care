from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import MedicalCareProfileUpdateForm
from .models import MedicalCareProfile


class MedicalCareProfileCreateView(SuccessMessageMixin, CreateView):
    model = MedicalCareProfile
    fields = "__all__"
    success_message = "Created"


class MedicalCareProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = MedicalCareProfile
    form_class = MedicalCareProfileUpdateForm
    success_message = "Updated"
    template_suffix_name = 'Update'

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)
from users.models import User

from .forms import MedicalCareProfileCreateForm, MedicalCareProfileUpdateForm
from .models import MedicalCareProfile


class MedicalCareProfileListView(LoginRequiredMixin, ListView):
    model = MedicalCareProfile


class MedicalCareProfileCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = MedicalCareProfile
    form_class = MedicalCareProfileCreateForm
    # fields = ['carer']
    success_message = "Created"

    # def get_success_url(self):
    #     return reverse("medical-care-profile-detail", args=(self.object.slug,))

    def get_initial(self):
        return {"carer": self.request.user.pk}

    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.carer = self.request.user
        form.save()
        return super(MedicalCareProfileCreateView, self).form_valid(form)


class MedicalCareProfileDetailView(LoginRequiredMixin, DetailView):
    model = MedicalCareProfile


class MedicalCareProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = MedicalCareProfile
    form_class = MedicalCareProfileUpdateForm
    success_message = "Updated"
    template_name_suffix = "_update_form"

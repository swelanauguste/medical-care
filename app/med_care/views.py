from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.views.generic.edit import FormMixin

from .forms import MedicalCareProfileCreateForm, MedicalCareProfileUpdateForm
from .models import MedicalCareProfile


class MedicalCareProfileCreateView(SuccessMessageMixin, CreateView):
    model = MedicalCareProfile
    form_class = MedicalCareProfileCreateForm
    # fields = ['carer']
    success_message = "Created"

    # def get_success_url(self):
    #     return reverse("clients:client-detail", args=(self.object.slug,))

    def get_initial(self):
        return {"carer": self.request.user.pk}

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.carer = self.request.user
        form.save()
        return super(MedicalCareProfileCreateView, self).form_valid(form)

    # def get_initial(self, *args, **kwargs):
    #     initial = super(MedicalCareProfileCreateView, self).get_initial()
    #     # initial.update({"carer": self.request.user})
    #     initial = initial.copy()
    #     initial["carer"] = self.request.user.pk
    #     return initial

    # def form_valid(self, form):
    #     form.instance.carer = self.request.user
    #     return super().form_valid(form)


class MedicalCareProfileUpdateView(SuccessMessageMixin, UpdateView):
    model = MedicalCareProfile
    form_class = MedicalCareProfileUpdateForm
    success_message = "Updated"
    template_name_suffix = "_update_form"

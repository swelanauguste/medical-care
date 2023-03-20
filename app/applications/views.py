from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import DetailView, ListView
from work.models import Work

from .forms import ApplicationCreateForm
from .models import Application


class ApplicationDetail(LoginRequiredMixin, DetailView):
    model = Application


class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    # ordering = ("-created_at",)
    # ordering = "created_at"

    def get_queryset(self):
        return Application.objects.filter(
            carer=self.request.user.carer_profile
        ).order_by("-created_at")


@login_required
def create_application_view(request, work_id):
    job = Work.objects.get(pk=work_id)
    if request.method == "POST":
        form = ApplicationCreateForm(data=request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.carer = request.user.carer_profile
            application.job = job
            application.save()
            messages.success(request, "Your application has been submitted")
            return HttpResponseRedirect(reverse("application-list"))
        else:
            messages.error(request, "Error")
    else:
        data = {"carer": request.user.carer_profile, "job": job}
        form = ApplicationCreateForm(initial=data)
    context = {"job": job, "form": form}
    return render(request, "applications/create_application.html", context)

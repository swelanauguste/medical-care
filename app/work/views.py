from django.views.generic import ListView

from .models import Work


class WorkListView(ListView):
    model = Work
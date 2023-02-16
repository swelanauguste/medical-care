from django.views.generic import ListView, DetailView

from .models import Work


class WorkListView(ListView):
    model = Work
    
    
class WorkDetailView(DetailView):
    model = Work
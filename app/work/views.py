from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Work


class WorkListView(ListView):
    model = Work
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Work.objects.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
                | Q(posted_by__profile__first_name__icontains=query)
                | Q(posted_by__profile__last_name__icontains=query)
                | Q(location__location_name__icontains=query)
            ).distinct()
        else:
            return Work.objects.all()
    
    
class WorkDetailView(DetailView):
    model = Work
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import DetailView, ListView
from users.models import Location

from .models import Work


class WorkListView(LoginRequiredMixin, ListView):
    model = Work
    
    extra_context = {'locations': Location.objects.all()}

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


class WorkDetailView(LoginRequiredMixin, DetailView):
    model = Work

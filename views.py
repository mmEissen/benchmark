import datetime

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Avg

from .models import Item


class ItemList(ListView):

    model = Item


class ItemDetails(DetailView):

    model = Item
    slug_field = 'name'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        time_deltas = [m.time_delta for m in self.object.measurement_set.all()]
        context['average'] = sum(time_deltas, datetime.timedelta()) / len(time_deltas)
        return context

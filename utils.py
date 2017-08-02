import datetime

from .models import Item, Measurement


def _build_name(func):
    return func.__module__ + '.' + func.__name__

def benchmark(func):
    fully_qualified_name = _build_name(func)
    def timing_function(*args, **kwargs):
        measurement = Measurement()
        measurement.start_time = datetime.datetime.now()

        result = func(*args, **kwargs)

        measurement.end_time = datetime.datetime.now()
        measurement.time_delta = measurement.end_time - measurement.start_time
        item, _ = Item.objects.get_or_create(name=fully_qualified_name)
        measurement.item = item
        measurement.save()
        return result
    return timing_function

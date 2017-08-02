import datetime

from .models import Item, Measurement

def benchmark(func):
    fully_qualified_name = func.__module__ + '.' + func.__name__
    def timing_function(*args, **kwargs):
        start = datetime.datetime.now()
        result = func(*args, **kwargs)
        end = datetime.datetime.now()
        duration = end - start
        item, _ = Item.objects.get_or_create(name=fully_qualified_name)
        Measurement.objects.create(item=item, time_delta=duration)
        return result
    return timing_function

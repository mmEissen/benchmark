from django.conf.urls import url

from .views import (
    ItemList,
    ItemDetails,
)


urlpatterns = [
    url(
        r'^$',
        ItemList.as_view(),
        name='benchmark-item-list',
    ),
    url(
        r'^(?P<slug>[-\w.]+)/$',
        ItemDetails.as_view(),
        name='benchmark-item-detail',
    ),
]

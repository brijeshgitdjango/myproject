from django.conf.urls import url
from .views import listview, detailview


urlpatterns = [
    
    url(r'^list/$', listview, name="list"),
    url(r'^detail/(?P<id>\d+)/$', detailview, name="detail"),
]

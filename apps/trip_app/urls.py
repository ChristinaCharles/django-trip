from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new_trip),
    url(r'^add_trip$', views.add_trip),
    url(r'^editing/(?P<id>\d+)$', views.edit),
    url(r'^edit/(?P<id>\d+)$', views.edit_trip),
    url(r'remove/(?P<id>\d+)$', views.remove),    
    url(r'un_join/(?P<id>\d+)$', views.un_join),
    url(r'join/(?P<id>\d+)$', views.join_trip),
    url(r'(?P<id>\d+)$', views.trip_page),
]
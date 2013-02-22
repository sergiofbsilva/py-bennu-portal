from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
      url(r'^head/(?P<hostname>.+)$',views.head, name='head'),
      url(r'^(?P<hostname>.+)$', views.index, name='index'),
)
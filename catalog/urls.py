from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^eventsdescript/$', views.EventsDescriptListView.as_view(), name='events_descript'),
    url(r'^events_descript/(?P<pk>\d+)$', views.EventsDescriptListView.as_view(), name='events_descript-detail'),
]

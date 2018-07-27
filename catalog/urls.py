from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^users/$', views.detail, name='users'),
    url(r'^eventsdescript/$', views.EventsDescriptListView.as_view(), name='events_descript'),
    url(r'^events_descript/(?P<pk>\d+)$', views.EventsDescriptListView.as_view(), name='events_descript-detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^users/$', views.UsersListView.as_view(), name='users'),
    url(r'^eventsdescript/$', views.EventsDescriptListView.as_view(), name='events_descript'),
    url(r'^eventsdescript/(?P<pk>\d+)$', views.EventsDescriptDetailView.as_view(), name='events_descript-detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

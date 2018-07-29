from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^users/$', views.UsersListView.as_view(), name='users'),
    url(r'^events_descript/$', views.EventsDescriptListView.as_view(), name='events_descript'),
    url(r'^events_descript/(?P<pk>\d+)$', views.EventsDescriptDetailView.as_view(), name='events_descript-detail'),
    url(r'^events_descript/new/$', views.EventsDescript_new.as_view(), name='events_descript-new'),
    url(r'^gift_descript/$', views.GiftDescriptListView.as_view(), name='gift_descript'),
    url(r'^gift_descript/(?P<pk>\d+)$', views.GiftDescriptDetailView.as_view(), name='gift_descript-detail'),
    url(r'^gift_outs/$', views.GiftOutsListView.as_view(), name='gift_outs'),
    url(r'^gift_outs/(?P<pk>\d+)$', views.GiftOutsDetailView.as_view(), name='gift_outs-detail'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

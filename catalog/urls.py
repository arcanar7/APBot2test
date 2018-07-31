from django.conf.urls import url, include
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^users/$', views.UsersListView.as_view(), name='users'),
    url(r'^users/(?P<pk>\d+)$', views.UsersDetailView.as_view(), name='users-detail'),
    url(r'^events_descript/$', views.EventsDescriptListView.as_view(), name='events_descript'),
    url(r'^events_descript/(?P<pk>\d+)$', views.EventsDescriptDetailView.as_view(), name='events_descript-detail'),
    url(r'^events_descript/new/$', views.EventsDescript_new.as_view(), name='events_descript-new'),
    url(r'^gift_descript/$', views.GiftDescriptListView.as_view(), name='gift_descript'),
    url(r'^gift_descript/(?P<pk>\d+)$', views.GiftDescriptDetailView.as_view(), name='gift_descript-detail'),
    url(r'^gift_descript/new/$', views.GiftDescript_new.as_view(), name='gift_descript-new'),
    url(r'^gift_outs/$', views.GiftOutsListView.as_view(), name='gift_outs'),
    url(r'^gift_outs/(?P<pk>\d+)$', views.GiftOutsDetailView.as_view(), name='gift_outs-detail'),
    url(r'^add_eventsgift/$', views.EventsGiftDetailView.as_view(), name='add_eventsgift'),
    url(r'^send_message/$', views.send_message, name='send_message'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

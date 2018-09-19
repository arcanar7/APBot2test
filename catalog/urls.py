from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', login_required(views.index), name='index'),
    url(r'^users/$', login_required(views.UsersListView.as_view()), name='users'),
    url(r'^users/(?P<pk>\d+)$', login_required(views.UsersDetailView.as_view()), name='users-detail'),
    url(r'^events_descript/$', login_required(views.EventsDescriptListView.as_view()), name='events_descript'),
    url(r'^events_descript/(?P<pk>\d+)$', login_required(views.EventsDescriptDetailView.as_view()), name='events_descript-detail'),
    url(r'^events_descript/new/$', login_required(views.EventsDescript_new.as_view()), name='events_descript-new'),
    url(r'^gift_descript/$', login_required(views.GiftDescriptListView.as_view()), name='gift_descript'),
    url(r'^gift_descript/(?P<pk>\d+)$', login_required(views.GiftDescriptDetailView.as_view()), name='gift_descript-detail'),
    # url(r'^gift_descript/new/$', login_required(views.GiftDescript_new.as_view()), name='gift_descript-new'),
    url(r'^gift_descript/new/$', login_required(views.add_gift), name='gift_descript-new'),
    url(r'^gift_outs/$', login_required(views.GiftOutsListView.as_view()), name='gift_outs'),
    url(r'^gift_outs/(?P<pk>\d+)$', login_required(views.GiftOutsDetailView.as_view()), name='gift_outs-detail'),
    url(r'^add_eventsgift/$', login_required(views.add_eventsgift), name='add_eventsgift'),
    url(r'^send_message/$', login_required(views.send_message), name='send_message'),
    url(r'^message_ok/$', login_required(views.message_ok), name='message_ok'),
    url(r'^message_error/$', login_required(views.message_error), name='message_error'),
]

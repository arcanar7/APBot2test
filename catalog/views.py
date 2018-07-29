from django.shortcuts import render
from .models import EventsDescript, EventsGift, Users, GiftDescript, GiftOuts
from django.views import generic
from telebot import TeleBot
from .config import token


def index(request):
    num_events_descript = EventsDescript.objects.all().count()
    num_users = Users.objects.all().count()
    num_events_gift = EventsGift.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context={'num_events_descript': num_events_descript, 'num_users': num_users,
                 'num_events_gift': num_events_gift},
    )


def send_message(request):
    users = Users.objects.all()
    bot = TeleBot(token)
    print(users)

    return render(
        request,
        'catalog/send_message.html',
        context={'users': users, 'bot': bot},
    )


class UsersListView(generic.ListView):
    model = Users
    paginate_by = 25


class EventsDescriptListView(generic.ListView):
    model = EventsDescript
    paginate_by = 25


class EventsDescriptDetailView(generic.UpdateView):
    model = EventsDescript
    template_name = "catalog/change_event.html"
    fields = ['name', 'descript']


class EventsDescript_new(generic.CreateView):
    model = EventsDescript
    template_name = "catalog/add_event.html"
    fields = ['name', 'descript']


class GiftDescriptListView(generic.ListView):
    model = GiftDescript
    paginate_by = 25


class GiftDescriptDetailView(generic.DetailView):
    model = GiftDescript


class GiftDescript_new(generic.CreateView):
    model = GiftDescript
    template_name = "catalog/add_gift.html"
    fields = ['name', 'cnt']


class GiftOutsListView(generic.ListView):
    model = GiftOuts
    paginate_by = 25


class GiftOutsDetailView(generic.DetailView):
    model = GiftOuts

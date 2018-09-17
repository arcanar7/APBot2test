from django.shortcuts import render, redirect
from .models import EventsDescript, Users, GiftDescript, GiftOuts
from django.views import generic
from telebot import TeleBot
from .config import token
from .forms import EventsGiftForm, SendMSG


def index(request):
    num_events_descript = EventsDescript.objects.all().count()
    num_users = Users.objects.all().count()
    num_gifts = GiftDescript.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_events_descript': num_events_descript, 'num_users': num_users,
                 'num_gifts': num_gifts},
    )


class UsersListView(generic.ListView):
    model = Users
    paginate_by = 25


class UsersDetailView(generic.DetailView):
    model = Users


class EventsDescriptListView(generic.ListView):
    model = EventsDescript
    paginate_by = 10


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


class GiftDescriptDetailView(generic.UpdateView):
    model = GiftDescript
    template_name = "catalog/change_gift.html"
    fields = ['name', 'cnt']


class GiftDescript_new(generic.CreateView):
    model = GiftDescript
    template_name = "catalog/add_gift.html"
    fields = ['name', 'cnt']


class GiftOutsListView(generic.ListView):
    model = GiftOuts
    paginate_by = 25


class GiftOutsDetailView(generic.UpdateView):
    model = GiftOuts
    template_name = "catalog/giftouts_detail.html"
    fields = ['status']


def add_eventsgift(request):
    events = EventsDescript.objects.all()
    gifts = GiftDescript.objects.all()
    if request.method == "POST":
        form = EventsGiftForm(request.POST)
        if form.is_valid():
            eventsgift = form.save(commit=False)
            eventsgift.id_event = request.POST['id_event']
            eventsgift.id_gift = request.POST['id_gift']
            eventsgift.save()
            return redirect('add_eventsgift')
    else:
        form = EventsGiftForm()

    return render(
        request,
        'catalog/add_eventsgift.html',
        context={'events': events, 'gifts': gifts, 'form': form},
    )


def send_message(request):
    users = list(Users.objects.all().values('id_user'))
    spisok1 = []
    for user in users:
        spisok1.append(user['id_user'])
    bot = TeleBot(token)
    form = SendMSG()
    if request.method == "POST":
        form = SendMSG(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            spisok = []
            if cd['contacts'] == '':
                spisok = set(spisok1)
            else:
                spisok = set(cd['contacts'].split(';'))
            for user in spisok:
                try:
                    bot.send_message(user, cd['msg'])
                except:
                    return redirect('message_error')
            return redirect('message_ok')

    return render(
        request,
        'catalog/send_message.html',
        context={'form': form},
    )


def message_ok(request):
    return render(
        request,
        'catalog/message_ok.html',
    )


def message_error(request):
    return render(
        request,
        'catalog/message_error.html',
    )

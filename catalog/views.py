from django.shortcuts import render, redirect
from .models import EventsDescript, EventsGift, Users, GiftDescript, GiftOuts
from django.views import generic
from telebot import TeleBot
from .config import token
from .forms import EventsGiftForm


def my_view(request):
    print("blablabla:")
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        print("Hello")
        return redirect('http://yandex.ru/')
        # redirect('%s/catalog/accounts/login/?next=/catalog/' % request.path)


def index(request):
    my_view(request)
    num_events_descript = EventsDescript.objects.all().count()
    num_users = Users.objects.all().count()
    num_gifts = GiftDescript.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context={'num_events_descript': num_events_descript, 'num_users': num_users,
                 'num_gifts': num_gifts},
    )


def send_message2():
    users = Users.objects.all()
    bot = TeleBot(token)
    for user in users:
        print(user)
        bot.send_message(user.id_user, "test message")


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


class EventsGiftDetailView(generic.CreateView):
    model = EventsGift
    fields = ['id_event', 'id_gift']
    template_name = "catalog/add_eventsgift.html"

    def all_events(self):
        return EventsDescript.objects.all()


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
    users = Users.objects.all()
    bot = TeleBot(token)
    print(users)



    return render(
        request,
        'catalog/send_message.html',
        context={'users': users, 'bot': bot},
    )
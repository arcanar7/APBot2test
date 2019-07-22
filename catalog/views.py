from django.shortcuts import render, redirect
from .models import EventsDescript, Users, GiftDescript, GiftOuts
from django.views import generic
from telebot import TeleBot
from .config import token
from .forms import EventsGiftForm, SendMSG, GiftDescriptForm
import django_excel as excel
from .markups import keyboardMain
import datetime
import logging
from time import sleep


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
    paginate_by = 200


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
    fields = ['name', 'cnt', 'img']


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
    form = SendMSG()
    if request.method == "POST":
        users = list(Users.objects.all().values('id_user'))
        spisok1 = []
        for user in users:
            spisok1.append(user['id_user'])
        funcount = 0
        bot = add_bot(funcount)
        form = SendMSG(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            spisok = []
            if cd['contacts'] == '':
                spisok = set(spisok1)
            else:
                spisok = set(cd['contacts'].split(';'))
            for user in spisok:
                try:
                    if cd['img'] is not None:
                        bot.send_photo(user, cd['img'], reply_markup=keyboardMain)
                    bot.send_message(user, cd['msg'], reply_markup=keyboardMain)
                    blocked_user(user, 'Не заблокирован')
                    sleep(0.04)
                except Exception as err:
                    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                                        filename=u'mylog.log')
                    logging.error(err)
                    if 'bot was blocked by the user' in str(err):
                        blocked_user(user, 'Заблокирован')
                    else:
                        return redirect('message_error')
            return redirect('message_ok')

    return render(
        request,
        'catalog/send_message.html',
        context={'form': form},
    )


def add_bot(count):
    count += 1
    try:
        bot = TeleBot(token)
        return bot
    except:
        if count < 10:
            sleep(10)
            bot = add_bot(count)
            return bot
        else:
            return count


def blocked_user(user, status):
    blockedUser = Users.objects.get(id_user=user)
    blockedUser.status = status
    blockedUser.dt_last_up = datetime.datetime.now()
    blockedUser.save()


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


def add_gift(request):
    form = GiftDescriptForm()
    if request.method == 'POST':
        form = GiftDescriptForm(request.POST, request.FILES)
        if form.is_valid():
            giftdescript = form.save(commit=False)
            giftdescript.name = request.POST['name']
            giftdescript.cnt = request.POST['cnt']
            giftdescript.img = request.FILES['img']
            giftdescript.save()
            return redirect('gift_descript')

    return render(
        request,
        'catalog/add_gift.html', {'form': form}
    )


def export_users(request):
    users = Users.objects.all()
    column_names = ['dt_add', 'id_user', 'id_invite', 'name', 'phone', 'dt_birth']
    return excel.make_response_from_query_sets(
        users,
        column_names,
        'xls',
        file_name="custom"
    )


def export_user(request, pk):
    users = Users.objects.filter(pk=pk)
    # user = Users.objects.get(pk=pk)
    # gifts = user.get_gifts()
    # stroka = ''
    # for gift in gifts:
    #     stroka += gift['gift_name'] + ", Статус: " + gift['status'] + "; \n"
    # users['Подарки'] = stroka
    column_names = ['dt_add', 'id_user', 'id_invite', 'name', 'phone', 'dt_birth']
    return excel.make_response_from_query_sets(
        users,
        column_names,
        'xls',
        file_name="custom"
    )


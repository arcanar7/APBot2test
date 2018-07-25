from django.shortcuts import render
from .models import EventsDescript, EventsGift, Users
from django.views import generic


def index(request):
    num_events_descript = EventsDescript.objects.all().count()
    num_users = Users.objects.all().count()
    num_events_gift = EventsGift.objects.all().count()

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context={'num_events_descript': num_events_descript, 'num_users': num_users, 'num_events_gift': num_events_gift},
    )


class EventsDescriptListView(generic.ListView):
    model = EventsDescript

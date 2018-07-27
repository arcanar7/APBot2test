from django.shortcuts import render, get_list_or_404
from .models import EventsDescript, EventsGift, Users
from django.views import generic


def index(request):
    num_events_descript = EventsDescript.objects.all().count()
    num_users = Users.objects.all().count()
    num_events_gift = EventsGift.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context={'num_events_descript': num_events_descript, 'num_users': num_users, 'num_events_gift': num_events_gift,
                 'num_visits': num_visits},
    )


def detail(request):
    user = get_list_or_404(Users)
    return render(request, 'catalog/detail.html', {'user': user})


class EventsDescriptListView(generic.ListView):
    model = EventsDescript

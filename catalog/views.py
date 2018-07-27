from django.shortcuts import render, get_list_or_404
from django.http import Http404
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
        context={'num_events_descript': num_events_descript, 'num_users': num_users,
                 'num_events_gift': num_events_gift},
    )


def detail(request):
    # try:
    #     users = Users.objects.all()
    # except Users.DoesNotExist:
    #     raise Http404("Question does not exist")
    users = get_list_or_404(Users)
    return render(request, 'catalog/detail.html', {'users': users})


class EventsDescriptListView(generic.ListView):
    model = EventsDescript


class EventsDescriptDetailView(generic.DetailView):
    model = EventsDescript


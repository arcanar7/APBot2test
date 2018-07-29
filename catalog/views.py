from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import Http404
from .models import EventsDescript, EventsGift, Users, GiftDescript, GiftOuts
from django.views import generic
from .forms import EventForm


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


def change_event(request, pk):
    event = get_object_or_404(EventsDescript, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        print(form)
        print(form.name)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('events_descript-detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'catalog/change_event.html', {'form': form})


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


class GiftDescriptListView(generic.ListView):
    model = GiftDescript
    paginate_by = 25


class GiftDescriptDetailView(generic.DetailView):
    model = GiftDescript


class GiftOutsListView(generic.ListView):
    model = GiftOuts
    paginate_by = 25


class GiftOutsDetailView(generic.DetailView):
    model = GiftOuts

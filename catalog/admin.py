from django.contrib import admin
from .models import EventsDescript, EventsGift, GiftDescript, GiftOuts, Users


@admin.register(EventsDescript)
class EventsDescriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'descript')


@admin.register(EventsGift)
class EventsGiftAdmin(admin.ModelAdmin):
    list_display = ('display_event', 'id_gift')


@admin.register(GiftDescript)
class GiftDescriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnt', 'img')


@admin.register(GiftOuts)
class GiftOutsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'status', 'id_event_gift')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('dt_add', 'id_user', 'id_invite', 'name', 'phone', 'dt_birth')

# Register your models here.

from django.contrib import admin
from .models import EventsDescript, EventsGift, GiftDescript, GiftOuts, Users


@admin.register(EventsDescript)
class EventsDescriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'descript')


@admin.register(EventsGift)
class EventsGiftAdmin(admin.ModelAdmin):
    list_display = ('display_event', 'display_gift')


@admin.register(GiftDescript)
class GiftDescriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnt', 'img')


@admin.register(GiftOuts)
class GiftOutsAdmin(admin.ModelAdmin):
    list_display = ('id_user', 'status', 'display_gift')


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ('dt_add', 'id_user', 'id_invite', 'name', 'phone', 'dt_birth', 'status', 'dt_last_up')

# Register your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EventsDescript(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name="Название события")
    descript = models.CharField(max_length=300, blank=True, null=True, verbose_name="Описание события")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events_descript-detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        managed = False
        db_table = 'events_descript'


class EventsGift(models.Model):
    id_event = models.IntegerField(blank=True, null=True, verbose_name="Название события")
    id_gift = models.IntegerField(blank=True, null=True, verbose_name="Название подарка")

    def __str__(self):
        return self.id_event

    def display_event(self):
        return EventsDescript.objects.filter(id=self.id_event).values("name")[0]['name']

    def display_gift(self):
        return GiftDescript.objects.filter(id=self.id_gift).values("name")[0]['name']

    display_event.short_description = 'Событие'
    display_gift.short_description = 'Подарок'

    class Meta:
        verbose_name = 'Подарки событий'
        verbose_name_plural = 'Подарки событий'
        managed = False
        db_table = 'events_gift'


class GiftDescript(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name="Название подарка")
    cnt = models.IntegerField(blank=True, null=True, verbose_name="Количество")
    img = models.CharField(max_length=300, blank=True, null=True, verbose_name="Картинка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список подарков'
        verbose_name_plural = 'Список подарков'
        managed = False
        db_table = 'gift_descript'


class GiftOuts(models.Model):
    id_user = models.CharField(max_length=30, blank=True, null=True, verbose_name="ID пользователя")
    status = models.CharField(max_length=50, blank=True, null=True, verbose_name="Статус")
    id_event_gift = models.IntegerField(blank=True, null=True, verbose_name="Название подарка")

    def __str__(self):
        return self.id_user

    def display_gift(self):
        gift = EventsGift.objects.filter(id=self.id_event_gift).values("id_gift")[0]['id_gift']
        return GiftDescript.objects.filter(id=gift).values("name")[0]['name']

    display_gift.short_description = 'Название подарка'

    class Meta:
        verbose_name = 'Подарки пользователей'
        verbose_name_plural = 'Подарки пользователей'
        managed = False
        db_table = 'gift_outs'


class Users(models.Model):
    dt_add = models.DateTimeField(blank=True, null=True, verbose_name="Дата регистрации")
    id_user = models.CharField(max_length=30, blank=True, null=True, verbose_name="ID пользователя")
    id_invite = models.CharField(max_length=300, blank=True, null=True, verbose_name="ID пригласившего")
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name="Имя пользователя")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Телефон")
    dt_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")

    # def __str__(self):
    #     return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        managed = False
        db_table = 'users'

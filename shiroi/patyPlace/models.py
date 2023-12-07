# Здесь описываются модели базы данных, то есть, создаешь здесь модель
# выполняешь миграции и в бд создается таблица, здесь происходит описание каждого поля определенной таблицы
from django.db import models


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class Party(models.Model):
    title = models.CharField(
        max_length=128, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    dt = models.DateField(max_length=20, verbose_name="Дата вечеринки")
    countPeople = models.IntegerField(verbose_name="Количество людей")
    adres = models.CharField(max_length=288, null=True,
                             verbose_name="Место проведения")
    images = models.ImageField(
        upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Обложка")
    creatorId = models.ForeignKey(AuthUser, models.DO_NOTHING, null=True)

    def get_absolute_url(self):
        return '/'


class FeedBack(models.Model):
    userField = models.ForeignKey(AuthUser, models.CASCADE)
    partyField = models.ForeignKey(Party, models.CASCADE)
    feedback = models.TextField()


class Party2User(models.Model):
    userField = models.ForeignKey(AuthUser, models.CASCADE)
    partyField = models.ForeignKey(Party, models.CASCADE)


class Booking(models.Model):
    party2user = models.ForeignKey(Party2User, models.CASCADE)
    book = models.BooleanField()

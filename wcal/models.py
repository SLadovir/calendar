from django.db import models
from django.urls import reverse
from django.utils import timezone


class Event(models.Model):
    # category = models.ForeignKey(settings.***AUTH_USER_MODEL***, on_delete=models.CASCADE)
    # То что между тремя звездочками надо будет заменить чтобы категории можно было выбирать работа, семья, прочее
    objects = None
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(blank=True, null=True)

    # x = event_date#хз
    def publish(self):
        self.created_date = timezone.now()
        # self.event_date = x#хз
        self.save()

    def __str__(self):
        return self.title  # + " " + category (то, что будет видно в редакторе, мб сначала категорию)


class EventDate(models.Model):  # сделаем страничку с днями такую же как и с событиями
    # и будем туда выводить day_detail.html
    date = models.ForeignKey(Event, on_delete=models.CASCADE)

# после изменений набрать в командной строке: python manage.py makemigrations wcal
# в dg(djangogirls) вместо Events написано Post
# Django создал для нас файл с миграцией для базы данных. Набери python manage.py migrate wcal /////(blog)
# python manage.py createsuperuser

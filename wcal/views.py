from django.shortcuts import render
from django.utils import timezone
from .models import Event
# Create your views here.
# кароч эта штука отвечает за представление всяких событий
def event_list(request):
    events = Event.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
    #dg-posts-events
    return render(request, 'wcal/event_list.html', {'events': events})
    # (исправления в двух местах !!!)в dg написано post_list вместо event_list
    # в dg написано blog вместо wcal
"""
чтобы протестить что-то на командной строке
командная строка:
    python manage.py shell
импорт класса Event:
    from wcal.models import Event
    from django.utils import timezone
    Event.objects.filter(event_date__lte=timezone.now())

"""

from datetime import datetime

from django.utils import timezone
from .models import Event
from django.shortcuts import render, get_object_or_404
from .forms import EventForm  # для формы добавления события (из текущего каталога)
from django.shortcuts import redirect  # для того чтобы после редактирования события мы сразу переходили к деталям


def day_detail(request, year=1970, month=1, day=2):  # работает с костылем(day - 1)
    events = Event.objects.order_by('event_date').filter(event_date__lte=datetime(
        year, month, day)).exclude(event_date__lte=datetime(year, month, day-1))  # - это типа
    # чтобы показывались события того года месяца и дня, которые в запросе
    return render(request, 'wcal/event_list.html', {'events': events})


def calendar(request):  # надо сделать чтобы создавался хтмлевский файл в нужную директорию
    # events = Event.objects.order_by('event_date')
    return render(request, 'wcal/calendar.html')


def event_list(request):  # это все события которые были и будут
    events = Event.objects.order_by('event_date')
    # также можно сделать чтобы показывались события которыетолько будут
    return render(request, 'wcal/event_list.html', {'events': events})


def past_event_list(request):  # это те события, которые уже прошли
    events = Event.objects.order_by('event_date').filter(event_date__lte=timezone.now())  # - это типа чтобы
    # показывались событя которые прошли
    return render(request, 'wcal/event_list.html', {'events': events})


def future_event_list(request):  # это те события, которые будут
    events = Event.objects.order_by('event_date').exclude(event_date__lte=timezone.now())  # - это типа чтобы
    # показывались событя которые будут
    return render(request, 'wcal/event_list.html', {'events': events})


def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'wcal/event_detail.html', {'event': event})


def event_new(request):
    if request.method == "POST":  # если мы отправяем тут форму, то все пойдет
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'wcal/event_edit.html', {'form': form})


def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":  # тут не меняем
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            # event.event_date = timezone.now() это кароч тема дляя блога чтобы у отредактированной записи сразу
            # появлялась дата публикации(но у нас не дата публикации а другая тема)
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'wcal/event_edit.html', {'form': form})


"""
чтобы протестить что-то на командной строке
командная строка:
    python manage.py shell
импорт класса Event:
    from wcal.models import Event
    from django.utils import timezone
    Event.objects.filter(event_date__lte=timezone.now())

"""

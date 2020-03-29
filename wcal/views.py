from django.shortcuts import render
from django.utils import timezone
from .models import Event
from django.shortcuts import render, get_object_or_404
from .forms import EventForm #для формы добавления события (из текущего каталога)
from django.shortcuts import redirect #для того чтобы после редактирования события мы сразу переходили к деталям события

# Create your views here.
# кароч эта штука отвечает за представление всяких событий
def event_list(request):
    events = Event.objects.filter(event_date__lte=timezone.now()).order_by('event_date')
    #dg-posts-events
    return render(request, 'wcal/event_list.html', {'events': events})
    # (исправления в двух местах !!!)в dg написано post_list вместо event_list
    # в dg написано blog вместо wcal
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'wcal/event_detail.html', {'event': event})

def event_new(request):
    form = EventForm()
    return render(request, 'wcal/event_edit.html', {'form': form})

def event_new(request):
    if request.method == "POST": #тут не надо переимменовывать POST!!!! (это метод)
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            #event.author = request.user - это нам не нужно, но пусть будет
            event.created_date = timezone.now()
            event.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = EventForm()
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

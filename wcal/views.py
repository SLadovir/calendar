from django.shortcuts import render
from django.utils import timezone
from .models import Event
from django.shortcuts import render, get_object_or_404
from .forms import EventForm #для формы добавления события (из текущего каталога)
from django.shortcuts import redirect #для того чтобы после редактирования события мы сразу переходили к деталям события

##### с сайта
'''
from .utils import Calendar

class CalendarView(ListView):
    model = Event
    template_name = 'components/calendar.html'
    success_url = reverse_lazy("calendar")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
'''
##### с сайта


# Create your views here.
# кароч эта штука отвечает за представление всяких событий
def event_list(request):#это все события которые были и будут
    events = Event.objects.order_by('event_date')#.filter(event_date__lte=timezone.now()) - это типа чтобы показывались событя которые прошли, также можно сделать чтобы показывались события которыетолько будут
    #dg-posts-events
    return render(request, 'wcal/event_list.html', {'events': events})
    # (исправления в двух местах !!!)в dg написано post_list вместо event_list
    # в dg написано blog вместо wcal

def day_detail(request, pk):
    events = Event.objects.order_by('event_date').filter(event_date__lte=pk) #- это типа чтобы показывались событя которые прошли, также можно сделать чтобы показывались события которыетолько будут
    return render(request, 'wcal/past_event_list.html', {'events': events})

def calendar(request):#
    return render(request, 'wcal/calendar.html')
'''
def future_event_list(request):#это те события, которые уже прошли -------- надо реализовать -----------
    events = Event.objects.order_by('event_date').filter(event_date__lte=timezone.now()) #- это типа чтобы показывались событя которые прошли, также можно сделать чтобы показывались события которыетолько будут
    return render(request, 'wcal/future_event_list.html', {'events': events})
'''
def past_event_list(request):#это те события, которые уже прошли -------- надо реализовать -----------
    events = Event.objects.order_by('event_date').filter(event_date__lte=timezone.now()) #- это типа чтобы показывались событя которые прошли, также можно сделать чтобы показывались события которыетолько будут
    return render(request, 'wcal/past_event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'wcal/event_detail.html', {'event': event})

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

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST": #тут не меняем
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            # event.event_date = timezone.now() это кароч тема дляя блога чтобы у отредактированной записи сразу появлялась дата публикации(но у нас не дата публикации а другая тема)
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

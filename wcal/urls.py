from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('past/', views.past_event_list, name='past_event_list'),
    path('future/', views.future_event_list, name='future_event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('calendar/', views.calendar, name='calendar'),

    path('calendar/<int:year>-<int:month>-<int:day>', views.day_detail, name='day_detail'),

    #    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    #    url(r’^calendar/$’, views.CalendarView.as_view(), name=’calendar’),
]

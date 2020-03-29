from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'), # (исправления в двух местах !!!)в dg написано post_list вместо event_list
]

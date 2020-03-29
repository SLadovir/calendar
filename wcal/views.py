from django.shortcuts import render

# Create your views here.
def event_list(request):
    return render(request, 'wcal/event_list.html', {})
    # (исправления в двух местах !!!)в dg написано post_list вместо event_list
    # в dg написано blog вместо wcal

from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Schedule

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'home.html'

class ScheduleCreateView(CreateView):
    model = Schedule
    template_name = 'schedule_new.html'
    fields = ['user', 'body']

    def get_success_url(self):
        return reverse('home')
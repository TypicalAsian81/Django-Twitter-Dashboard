from django.urls import path
from .views import ScheduleListView, ScheduleCreateView

urlpatterns = [
    path('schedule/new/', ScheduleCreateView.as_view(), name='schedule_new'),
    path('', ScheduleListView.as_view(), name='home'),
]
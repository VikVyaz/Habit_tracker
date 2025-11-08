from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import (MyUsefulHabitListView, PleasantHabitViewSet,
                    PublicUsefulHabitListView, RewordViewSet,
                    UsefulHabitCreateView, UsefulHabitDestroyView,
                    UsefulHabitRetrieveView, UsefulHabitUpdateView)

app_name = HabitsConfig.name

router1 = DefaultRouter()
router2 = DefaultRouter()
router1.register(r"reword", RewordViewSet, basename="reword")
router2.register(r"pleasant_habit", PleasantHabitViewSet, basename="pleasant_habit")

urlpatterns = [
    path('useful_habit/my_habits/list/', MyUsefulHabitListView.as_view(), name='useful_my_list'),
    path('useful_habit/public_habits/list/', PublicUsefulHabitListView.as_view(), name='useful_public_list'),
    path('useful_habit/create/', UsefulHabitCreateView.as_view(), name='useful_create'),
    path('useful_habit/<int:pk>/', UsefulHabitRetrieveView.as_view(), name='useful_detail'),
    path('useful_habit/<int:pk>/update/', UsefulHabitUpdateView.as_view(), name='useful_update'),
    path('useful_habit/<int:pk>/delete/', UsefulHabitDestroyView.as_view(), name='useful_delete')
] + router1.urls + router2.urls

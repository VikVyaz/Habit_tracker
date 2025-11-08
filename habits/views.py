from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from habits.models import PleasantHabit, Reword, UsefulHabit
from habits.paginators import HabitPaginator, RewordPaginator
from habits.permissions import HabitPermission
from habits.serializers import (PleasantHabitSerializer, RewordSerializer,
                                UsefulHabitSerializer)
from habits.tasks import send_simple_notification


class RewordViewSet(viewsets.ModelViewSet):
    """ViewSet для Reword"""

    queryset = Reword.objects.all()
    serializer_class = RewordSerializer
    pagination_class = RewordPaginator


class PleasantHabitViewSet(viewsets.ModelViewSet):
    """ViewSet для PleasantHabit"""

    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MyUsefulHabitListView(generics.ListAPIView):
    """List view для UsefulHabit, где авторизированный пользователь является хозяином привычки"""

    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = UsefulHabit.objects.all()

        return queryset.filter(owner=user)


class PublicUsefulHabitListView(generics.ListAPIView):
    """List view для публичных UsefulHabit(is_public==True)"""

    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def get_queryset(self):
        queryset = UsefulHabit.objects.all()

        return queryset.filter(is_public=True)


class UsefulHabitCreateView(generics.CreateAPIView):
    """Create view для UsefulHabit"""

    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def perform_create(self, serializer):
        habit = serializer.save(owner=self.request.user)
        send_simple_notification.delay(
            f'Привычка "{habit.name}" создана.',
            habit.owner.telegram_chat_id
        )


class UsefulHabitRetrieveView(generics.RetrieveAPIView):
    """Retrieve view для UsefulHabit"""

    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]


class UsefulHabitUpdateView(generics.UpdateAPIView):
    """Update view для UsefulHabit"""

    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def perform_update(self, serializer):
        habit = serializer.save()
        send_simple_notification.delay(
            f'Привычка "{habit.name}" изменена.',
            habit.owner.telegram_chat_id
        )


class UsefulHabitDestroyView(generics.DestroyAPIView):
    """Destroy view для UsefulHabit"""

    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, HabitPermission]

    def perform_destroy(self, instance):
        send_simple_notification.delay(
            f'Привычка "{instance.name}" удалена.',
            instance.owner.telegram_chat_id
        )
        instance.delete()

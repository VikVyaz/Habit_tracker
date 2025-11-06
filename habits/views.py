from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from habits.models import PleasantHabit, Reword, UsefulHabit
from habits.paginators import HabitPaginator, RewordPaginator
from habits.permissions import HabitPermission
from habits.serializers import PleasantHabitSerializer, UsefulHabitSerializer, RewordSerializer


class RewordViewSet(viewsets.ModelViewSet):
    queryset = Reword.objects.all()
    serializer_class = RewordSerializer
    pagination_class = RewordPaginator


class PleasantHabitViewSet(viewsets.ModelViewSet):
    queryset = PleasantHabit.objects.all()
    serializer_class = PleasantHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]


class UsefulHabitListView(generics.ListAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]

    def get_queryset(self):
        user = self.request.user
        queryset = UsefulHabit.objects.all()

        return queryset.filter(owner=user)


class UsefulHabitCreateView(generics.CreateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]


class UsefulHabitRetrieveView(generics.RetrieveAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]


class UsefulHabitUpdateView(generics.UpdateAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]


class UsefulHabitDestroyView(generics.DestroyAPIView):
    queryset = UsefulHabit.objects.all()
    serializer_class = UsefulHabitSerializer
    pagination_class = HabitPaginator
    # permission_classes = [IsAuthenticated, HabitPermission]

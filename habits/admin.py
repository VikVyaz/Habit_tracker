from django.contrib import admin

from habits.models import PleasantHabit, Reword, UsefulHabit


@admin.register(PleasantHabit)
class PleasantAdmin(admin.ModelAdmin):
    """Доступ для админки для PleasantHabit"""

    list_display = [field.name for field in PleasantHabit._meta.fields]


@admin.register(UsefulHabit)
class UsefulAdmin(admin.ModelAdmin):
    """Доступ для админки для PleasantHabit"""

    list_display = [field.name for field in UsefulHabit._meta.fields]


@admin.register(Reword)
class RewordAdmin(admin.ModelAdmin):
    """Доступ для админки для Reword"""

    list_display = [field.name for field in Reword._meta.fields]

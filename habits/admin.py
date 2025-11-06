from django.contrib import admin

from habits.models import PleasantHabit, UsefulHabit, Reword


@admin.register(PleasantHabit)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PleasantHabit._meta.fields]


@admin.register(UsefulHabit)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UsefulHabit._meta.fields]


@admin.register(Reword)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reword._meta.fields]

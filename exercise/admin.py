from django.contrib import admin
from .models import Exercise, Routine

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")
    search_fields = ("name",)


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "weekday", "time", "created_at")
    list_filter = ("weekday", "user")
    search_fields = ("name", "user__username")
    ordering = ("weekday", "time")    
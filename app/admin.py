from django.contrib import admin

# Register your models here.
from app.models import step_count,calories_burnt, distance_covered,heart_rate

@admin.register(step_count)
class step_countAdmin(admin.ModelAdmin):
    pass

@admin.register(calories_burnt)
class calories_burntAdmin(admin.ModelAdmin):
    pass

@admin.register(distance_covered)
class distance_coveredAdmin(admin.ModelAdmin):
    pass

@admin.register(heart_rate)
class heart_rateAdmin(admin.ModelAdmin):
    pass
from django.contrib import admin
from .models import Profile, Exercise, Workout, Tracker, Entry  
# Register your models here.

admin.site.register(Profile)
admin.site.register(Exercise)
admin.site.register(Workout)
admin.site.register(Tracker)
admin.site.register(Entry)
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.db.models.fields.related import ManyToManyField 


#1 Profile has 1 user 
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="images", null=True)

    def __str__(self):
        return self.user.username 


class Exercise(Model):
    name = models.CharField(max_length=50) 
    image = models.CharField(max_length=5000) 
    description = models.TextField() 

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']

#Many Workouts have many exercises. Many Exercises have many workouts. 
class Workout(Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    exercises = ManyToManyField(Exercise, blank=True)

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']

#One Tracker has One User 
#One Tracker has one workout, One workout has many trackers 

class Tracker(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tracked_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date_custom = models.DateTimeField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username}: {self.date_custom} - {self.tracked_workout}'

    class Meta:
        ordering = ['date_custom']
    
#One entry has one author. One author has many entries. 
#One entry has one exercise. One exercise has many entries 
#One entry has one tracker. One tracker has many entries 

class Entry(Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    entry_exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    tracker = models.ForeignKey(Tracker, on_delete=models.CASCADE)
    date_custom = models.DateTimeField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    set_one = models.CharField(max_length=2, default=0, null=True, blank=True)
    set_two = models.CharField(max_length=2, default=0, null=True, blank=True)
    set_three = models.CharField(max_length=2, default=0, null=True, blank=True)
    set_four = models.CharField(max_length=2, default=0, null=True, blank=True)
    set_five = models.CharField(max_length=2, default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.author}: {self.date_custom} - {self.tracker}'

    class Meta:
        ordering = ['date_custom']


from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User



#1 Profile has 1 user 
class Profile(Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    join_date = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to="images", null=True)

    def __str__(self):
        return self.user.username 

class Workout(Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']

#A exercise has one workout. A workout has many exercises 
class Exercise(Model):
    name = models.CharField(max_length=50) 
    image = models.CharField(max_length=5000) 
    description = models.TextField() 
    related_workout = models.ForeignKey(Workout, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        ordering = ['name']

class Tracker(Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_custom = models.DateField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.date_custom} - {self.date_creation}'

    class Meta:
        ordering = ['date_custom']
    
#One entry has one author. One author has many entries. 
#One entry has one exercise. One exercise has many entries 
#One entry has one tracker. One tracker has many entries 

class Entry(Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    entry_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date_custom = models.DateField(null=True, blank=True)
    date_creation = models.DateField(auto_now_add=True)
    set1 = models.BooleanField(default=False)
    set2 = models.BooleanField(default=False)
    set3 = models.BooleanField(default=False)
    set4 = models.BooleanField(default=False)
    set5 = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f'{self.author}: {self.date_custom}'

    class Meta:
        ordering = ['date_custom']














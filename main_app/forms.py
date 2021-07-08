from django import forms 
from django.forms import ModelForm 
from .models import Workout 


class ProfileForm(forms.Form):
    user_image = forms.FileField()

class WorkoutCreateForm(ModelForm):
    class Meta:
        model = Workout 
        fields = [
            'name',
            'description',
            'custom_exercise_one',
            'custom_exercise_two',
            'custom_exercise_three',
            'custom_exercise_four',
            'custom_exercise_five',
            'custom_exercise_six',
            'custom_exercise_seven',
            'custom_exercise_eight'
        ] 
        



    
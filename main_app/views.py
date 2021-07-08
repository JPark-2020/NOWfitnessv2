from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View  
from django.views.generic.base import TemplateView 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse 
from django.contrib.auth.models import User
from django.core.paginator import Paginator 
from .models import Profile, Exercise, Tracker, Entry, Workout 
from .forms import ProfileForm 

class Home(TemplateView):
    template_name = "home.html" 

class SignUp(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) 
            login(request,user)
            return redirect("/profile/")
        else:
            return redirect("/")
    
class Workouts(View):
    def get(self, request):
        admin_workouts = Workout.objects.filter(admin_created=True)
        context = {"admin_workouts": admin_workouts}
        return render(request, "workouts/workouts.html", context)
    
class Workouts_Detail(View):

    def get(self, request, type):        
        if type == "boxing":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Boxing")[0]
            exercises = Exercise.objects.filter(category="Boxing")
            workoutHTML = "workouts/boxing.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts/workouts-detail.html", context)

        elif type == "yoga":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Yoga")[0]
            exercises = Exercise.objects.filter(category="Yoga")
            workoutHTML = "workouts/yoga.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts/workouts-detail.html", context)

        elif type == "bodyweight":
            newType = type.capitalize()
            workout = Workout.objects.filter(name="Bodyweight")[0]
            exercises = Exercise.objects.filter(category="Bodyweight")
            workoutHTML = "workouts/bodyweight.html"
            context = {"workout":workout, "exercises":exercises, "type":newType, "workoutHTML":workoutHTML}
            return render(request, "workouts/workouts-detail.html", context)

def store_file(file):
    with open("temp/image.jpg", "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class Profiles(View):
    def get(self, request):
        user_profile = Profile.objects.get(user_id=request.user)
        form = ProfileForm()
        context = {"form":form, "user_profile":user_profile}
        return render(request, 'profile.html', context)

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        context = {"form":submitted_form}
        user_profile = Profile.objects.get(user=request.user)

        if submitted_form.is_valid():
            user_profile.image = request.FILES["user_image"]
            user_profile.save()
            
            return HttpResponseRedirect('/profile/')

        return render(request, 'profile.html', context)
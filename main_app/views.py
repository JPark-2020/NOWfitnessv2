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
from .forms import ProfileForm, WorkoutCreateForm  
from django.db.models import Q 

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


class Profiles(View):
    def get(self, request):
        user_profile = Profile.objects.get(user_id=request.user)
        form = ProfileForm()
        form2 = WorkoutCreateForm()
        user_workouts = Workout.objects.filter(Q(author_id=request.user.id) & Q(admin_created=False))
        context = {"form":form, "user_profile":user_profile, "form2":form2, "user_workouts":user_workouts}
        return render(request, 'profile/profile.html', context)

    def post(self, request):
        usersID = request.user 

        if 'user_image' in request.FILES:
            submitted_form = ProfileForm(request.POST, request.FILES)
            context = {"form":submitted_form}
            userProfile = Profile.objects.get(user_id=usersID.id)

            if submitted_form.is_valid():
                userProfile.image = request.FILES["user_image"]
                userProfile.save()
                
                return HttpResponseRedirect('/profile/')

        if 'name' in request.POST:
            form2 = WorkoutCreateForm(request.POST)
            context = {"form2":form2}

            if form2.is_valid():
                user_workout = form2.save(commit=False)
                user_workout.author = User.objects.get(id=self.request.user.id)
                Exercise.objects.create(name=user_workout.custom_exercise_one.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_two.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_three.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_four.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_five.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_six.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_seven.upper(), category=user_workout.name, creator=self.request.user)
                Exercise.objects.create(name=user_workout.custom_exercise_eight.upper(), category=user_workout.name, creator=self.request.user)
                form2.save()
                return HttpResponseRedirect('/profile/')

        return render(request, 'profile/profile.html', context)

class ProfilesWorkouts(View):
    def get(self, request, workoutname):
        if workoutname:
            print(workoutname)
            found_user_workout = Workout.objects.get(name=workoutname)
            context = {"found_user_workout":found_user_workout}
            return render(request, 'profile/myworkoutinfo.html', context)

    def post(self, request, workoutname):
        found_user_workout = Workout.objects.get(name=workoutname)
        found_user_workout.delete()
        return HttpResponseRedirect('/profile/')










class Entries(View):
    def get(self, request):
        user_workouts = Workout.objects.filter(author_id=request.user.id)

        
        # context = {"user_workouts":user_workouts}
        usersID = request.user 
        userProfile = Profile.objects.get(user_id=usersID.id)
        user_entries = Entry.objects.filter(author_id=usersID.id)
        
        paginator = Paginator(user_entries, 16)
        page = request.GET.get('pg')
        user_entries = paginator.get_page(page)

        context = {"user_entries":user_entries, "userProfile":userProfile}
        return render(request, 'entries/entries.html', context)

class EntryCreate(CreateView):
    model = Entry 
    fields = ['entry_exercise','set_one', 'set_two', 'set_three', 'set_four', 'set_five', 'tracker']
    template_name = "entries/entry-create.html"
    
    def get_success_url(self):
        return reverse('entry-detail', kwargs={'pk': self.object.pk})


class EntryDetail(DetailView):
    model = Entry 
    template_name = "entries/entry-detail.html"


class EntryUpdate(UpdateView):
    model = Entry 
    fields = ['entry_exercise','set_one', 'set_two', 'set_three', 'set_four', 'set_five', 'tracker']
    template_name = "entries/entry-update.html"

    def get_success_url(self):
        return reverse('entry-detail', kwargs={'pk': self.object.pk})

class EntryDelete(DeleteView):
    model = Entry 
    template_name = "entries/entry-delete.html"
    
    def get_success_url(self):
        return reverse('entries-page')


class Tracker_Page(View):
    def get(self, request):
        usersID = request.user 
        user_entries = Entry.objects.filter(author_id=usersID.id)
        context = {"user_entries":user_entries}
        return render(request, 'tracker.html', context)


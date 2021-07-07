from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
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


class Home(TemplateView):
    template_name = "home.html" 

class About(TemplateView):
    template_name ="about.html"

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
            return redirect("/")
        else:
            return redirect("/")
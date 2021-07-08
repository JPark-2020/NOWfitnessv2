from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home-page"),
    path('about/', views.About.as_view(), name="about-page"),
    path('accounts/signup', views.SignUp.as_view(), name="signup"),
    path('workouts/', views.Workouts.as_view(), name="workouts-page"),
    path('workouts/<str:type>', views.Workouts_Detail.as_view(), name="workouts-detail-page"),
]

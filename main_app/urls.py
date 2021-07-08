from django.urls import path
from . import views 

urlpatterns = [
    path('', views.Home.as_view(), name="home-page"),
    path('profile/',views.Profiles.as_view(), name="profile-page"),
    path('profile/<str:workoutname>', views.ProfilesWorkouts.as_view(), name="myworkout"),
    path('accounts/signup', views.SignUp.as_view(), name="signup"),
    path('workouts/', views.Workouts.as_view(), name="workouts-page"),
    path('workouts/<str:type>', views.Workouts_Detail.as_view(), name="workouts-detail-page"),
    path('entries/', views.Entries.as_view(), name="entries-page"),
    path('entries/new', views.EntryCreate.as_view(), name="entry-create"),
    path('entries/<int:pk>/', views.EntryDetail.as_view(), name="entry-detail"),
    path('entries/<int:pk>/update',views.EntryUpdate.as_view(), name="entry-update"),
    path('entries/<int:pk>/delete/', views.EntryDelete.as_view(), name="entry-delete"),
    path('tracker/', views.Tracker_Page.as_view(), name="tracker-page"),
]

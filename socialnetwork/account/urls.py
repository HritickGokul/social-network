from django.urls import path
from django.contrib.auth import views as auth_views
from . import views



app_name = 'account'

urlpatterns = [
    path('signup/' , views.SignUp.as_view() , name = 'signup'),
    path('logout/' , auth_views.LogoutView.as_view() , name = 'logout'),
    path('login/' , auth_views.LoginView.as_view(template_name = 'account/login.html') , name = 'login'),
    path('suggestion/' , views.Suggestion.as_view() , name = 'suggestion'),
    path('profile/<slug:slugg>/' , views.profile , name = 'profile'),
    path('profile/<slug:slugg>/edit/' , views.profile_edit , name = 'profile_edit'),
    path('profile/<slug:slugg>/follow/' , views.add_follower , name = 'add_follower'),
    path('search/' , views.search_user , name = 'search_user'),
]

"""goodmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from movies import views
from movies.views import MovieListView

urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movie_list, name="movie_list"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.profile_view, name="user_profile"),
    path("accounts/signup/", views.user_signup, name="user_signup"),
    path("accounts/login/", include("django.contrib.auth.urls"), name="login"),
    path("admin/", admin.site.urls),
    path("about/", MovieListView.as_view()),
]

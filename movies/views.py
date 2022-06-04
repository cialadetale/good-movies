from datetime import datetime
import re
from django.shortcuts import render
from movies.models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView

# Create your views here.


def index(request):
    return render(request, "index.html")


class MovieListView(ListView):
    model = Movie
    template_name = "movie_list.html"


def movie_list(request):
    movies_from_db = Movie.objects.all()
    context = {"movies": movies_from_db, "date": datetime.now()}
    return render(request, "movie_list.html", context)


def profile_view(request):
    return render(request, "profile.html")


def user_signup(request):
    if request.method == "POST":
        # tu trzeba przetworzyć dane z formularza
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # tutaj obsługujemy przypadek kiedy użytkownik pierwszy raz wyświetlił stronę
        form = UserCreationForm()

    # na końcu zwracamy wyrenderowanego HTMLa
    return render(
        request, template_name="registration/signup_form.html", context={"form": form}
    )


def login(request):
    return render(request, "login.html")

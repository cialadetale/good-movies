from datetime import datetime
from turtle import title
from django.test import TestCase
from .models import Movie

# Create your tests here.

class TestMovies(TestCase):
    def setUp(self):
        Movie.objects.create(title="test", published_at=datetime.now())
        Movie.objects.create(title="shrek", published_at=datetime.now())

    def test_true(self):
        assert 1 == 1

    def test_get_movie(self):
        assert Movie.objects.get(title="test")
        assert Movie.objects.get(title="shrek")

    def test_movie_count(self):
        assert Movie.objects.count() == 2
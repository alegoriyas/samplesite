"""
Definition of urls for bboard.
"""

from django.urls import path
from . import views
from .views import HomeView, by_rubric

urlpatterns = [
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', views.HomeView, name="home"),
]


"""
Definition of urls for bboard.
"""

from django.urls import path
from . import views
from .views import hello

urlpatterns = [
    path('', hello, name ='hello'),
]
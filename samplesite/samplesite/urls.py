"""
Definition of urls for samplesite.
"""

from django.urls import path, include
from django.contrib import admin



urlpatterns = [
    path('', include('bboard.urls')),
    path('admin/', admin.site.urls),
]
from django.urls import path, include

from catalog.views import contacts, home

urlpatterns = [
    path('', contacts, home),
]

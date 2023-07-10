from django.urls import path, include

from catalog.views import index, contacts, home

urlpatterns = [
    path('', index, contacts, home),
]

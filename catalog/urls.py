from django.urls import path, include

from catalog.views import contacts, home

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]

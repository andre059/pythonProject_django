from django.urls import path, include

from main.views import index

urlpatterns = [
    path('', index),
]

#  path('', include('students.urls', namespace='students')),
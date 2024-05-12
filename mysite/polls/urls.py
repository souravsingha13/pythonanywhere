from django.urls import path
from .views import polls


urlpatterns = [
    path('', polls, name='index'),
]

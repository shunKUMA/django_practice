from django.urls import path
from .views import hello_appview


urlpatterns = [
    path('hello_app/', hello_appview),
]

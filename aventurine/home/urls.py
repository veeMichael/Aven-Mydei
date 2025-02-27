from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("mydei", views.character2, name="mydei"),
]

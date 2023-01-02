from django.urls import path
from . import views


urlpatterns = [
    path("", views.index_page, name='home'),
    path("<str:name>", views.greet, name='greet'),
]
from django.urls import path

from .views import HomeView, PostsView


urlpatterns = [
    path('', HomeView.as_view()),
    path('posts/', PostsView.as_view()),
]

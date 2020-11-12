from django.urls import path

from .views import HomeView, PostsView


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name='my_posts'),
]

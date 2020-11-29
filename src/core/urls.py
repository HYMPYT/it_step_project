from django.urls import path

from .views import HomeView, PostsView, PostCreateView, AboutView, FriendsView


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('friends/', FriendsView.as_view(), name='my_friends'),
    path('posts/', PostsView.as_view(), name='my_posts'),
    path('posts/create/', PostCreateView.as_view(), name='post_creation')
]

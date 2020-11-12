from django.views.generic import ListView
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


class HomeView(ListView):
    """Home view"""
    template_name = 'core/news.html'
    queryset = Post.objects.filter(is_active=True)

class PostsView(ListView):
    """Posts view"""
    template_name = 'core/news.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Returns active posters posts"""
        return Post.objects.filter(is_active=True, poster=self.request.user)

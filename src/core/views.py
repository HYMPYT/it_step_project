from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import Post


class HomeView(ListView):
    """Home view"""
    template_name = 'core/news.html'

    def get_queryset(self):
        return Post.objects.exclude(is_active=False).exclude(poster=self.request.user)

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

class PostsView(ListView):
    """Posts view"""
    template_name = 'core/news.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        """Returns active posters posts"""
        return Post.objects.filter(is_active=True, poster=self.request.user)

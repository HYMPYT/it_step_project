from django.views.generic import ListView, CreateView, TemplateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.template.response import TemplateResponse

from .forms import PostCreationForm
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


class PostCreateView(CreateView):
    """This view provides post creation by form"""
    template_name = 'core/post_creation.html'
    form_class = PostCreationForm
    model = Post

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        
        form.save(user=request.user)

        return redirect('core:my_posts')

class FriendsView(TemplateView):
    """Friends view"""
    template_name = 'core/friends.html'

class AboutView(TemplateView):
    """About view"""
    template_name = 'core/about.html'



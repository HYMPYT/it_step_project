from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


class Card:
    def __init__(self, title: str, body: str):
        self.title = title
        self.body = body

    def __str__(self):
        return self.title

def home(request, *args, **kwars) -> HttpResponse:
    """Home view"""

    

    ctx = {
        'posts': Post.objects.all()
    }

    return render(request, 'core/index.html', context=ctx)

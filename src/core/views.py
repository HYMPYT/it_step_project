from django.http import HttpResponse

def home(request, *args, **kwars) -> HttpResponse:
    """Home view"""
    # TODO Resume from here
    return HttpResponse('<h1 style="color: green; font-size: 70px; text-align: center">Home page</h1>')

def about(request, *args, **kwars) -> HttpResponse:
    """About view"""
    return HttpResponse('<h1 style="color: green; font-size: 70px; text-align: center">About page</h1>')
from django.http import HttpResponse

def home(request, *args, **kwars) -> HttpResponse:
    """Home view"""
    return HttpResponse('<h1 style="color: green; font-size: 70px; text-align: center">Home page</h1>')
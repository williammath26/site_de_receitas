from django.shortcuts import render
from django.http import HttpResponse


# HTTP REQUESTS
# HTTP RESPONSE
# Create your views here.
# RETURN HTTP RESPONSE
    
def home(request):
    return render(request, "home.html",context={
        'name':'Django'
    })


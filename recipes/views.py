from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe

# HTTP REQUESTS
# HTTP RESPONSE
# Create your views here.
# RETURN HTTP RESPONSE
    
def home(request):
    return render(request, "pages/home.html",context={
        'recipes':[make_recipe() for _ in range(10)]
    })

def recipe(request,id):
    return render(request, "pages/recipe-view.html",context={
        recipe:make_recipe(),
    })

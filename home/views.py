from django.shortcuts import render

# Create your views here.
def index(request):
    """ renders an index page"""
    return render(request, 'index.html')
from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create a hello world view
def index(request):
    return HttpResponse("Hello, world! You're at the polls index...");

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Bug

# Create your views here.
def index(request):
    bugs = Bug.objects.all()
    return render(request, 'index.html', {'all_bug': bugs})
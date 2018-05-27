from django.shortcuts import render
from django.http import HttpResponse
from .models import Presidium

# Create your views here.
def index(request):
    people = Presidium.objects.all()
    return render(request, 'index.html', {'people': people})
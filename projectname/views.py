from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'text': 'This is the index.'}
    return render(request, 'index.html', context)
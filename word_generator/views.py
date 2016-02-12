from django.shortcuts import render

# Create your views here.

def word_generator_home(request):
    context = {}
    return render(request, 'word_generator_home.html', context)

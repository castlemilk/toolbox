from django.shortcuts import render
from forms import PostalCodeForm
from django import forms
# from models import AAAData
# Create your views here.
def fuel_price_home(request):
    form = PostalCodeForm(request.POST or None)
    context = {
        "form": form,
    }
    print form.is_valid()
    if form.is_valid():
        context = {
            "form": form,
        }



    return render(request, 'fuel_price_home.html', context)


def fuel_price_graphs(request):

    context = {}
    return render(request, 'fuel_price_graphs.html', context)

def fuel_price_information(request):

    context = {}
    return render(request, 'fuel_price_information.html', context)

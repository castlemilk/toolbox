from django.shortcuts import render

# Create your views here.
def fuel_price_home(request):
    context = {}

    return render(request, 'fuel_price_home.html', context)


def fuel_price_graphs(request):

    context = {}
    return render(request, 'fuel_price_graphs.html', context)

def fuel_price_information(request):

    context = {}
    return render(request, 'fuel_price_information.html', context)

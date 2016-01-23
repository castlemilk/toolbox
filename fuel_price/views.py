from django.shortcuts import render
from forms import LocationForm
from . import models
import autocomplete_light.shortcuts as al
import json
al.autodiscover()
# from models import AAAData
# Create your views here.
def fuel_price_home(request):
    form = LocationForm(request.POST or None)
    locations = models.AAAData.objects.all()
    # for key,item in form.fields.iteritems():
    #     print key, item

    context = {
        "form": form,
        # "locations":locations,
    }
    # print form.is_valid()
    if form.is_valid():
        pk = form.cleaned_data['location']
        location =models.AAAData.objects.filter(pk=pk)[0]
        variables = location.data.keys()
        fuel_data = sorted(location.data.iteritems())
        variables = sorted([x.replace(' ', '_') for x in variables])
        print variables
        if models.OilPrice.objects.filter(oil_type='brent'):
            brent_data = models.OilPrice.objects.filter(oil_type='brent')[0].data
        else:
            brent_data = None


        context = {
            "form": form,
            "fuel_data": fuel_data,
            "variables": variables,
            "fuel_data_json": json.dumps(fuel_data),
            "brent_data_json": json.dumps(brent_data),
        }



    return render(request, 'fuel_price_home.html', context)


def fuel_price_graphs(request):

    context = {}
    return render(request, 'fuel_price_graphs.html', context)

def fuel_price_information(request):

    context = {}
    return render(request, 'fuel_price_information.html', context)

from django.conf.urls import url, include
import autocomplete_light
from fuel_price.models import AAAData
autocomplete_light.registry.autocomplete_model_base = AAAData
from fuel_price import views

# import autocomplete_light
# autocomplete_light.autodiscover()
urlpatterns = [
                url(r'^fuel_price$', views.fuel_price_home, name = 'fuel_price_home'),
                url(r'^fuel_price/graphs', views.fuel_price_graphs,
                name='fuel_price_graphs'),
                url(r'^fuel_price/information', views.fuel_price_information,
                name='fueL_price_graphs'),
                url(r'autocomplete/', include('autocomplete_light.urls')),
              ]

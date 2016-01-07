from django.conf.urls import url
from fuel_price import views
urlpatterns = [
                url(r'^fuel_price$', views.fuel_price_home, name = 'fuel_price_home'),
                url(r'^fuel_price/graphs', views.fuel_price_graphs,
                name='fuel_price_graphs'),
                url(r'^fuel_price/information', views.fuel_price_information,
                name='fueL_price_graphs'),
              ]

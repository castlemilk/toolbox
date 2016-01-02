# finance app urls:
from django.conf.urls import url
from finance import views
urlpatterns = [
                url(r'^finance$', views.list_tools, name = 'finance_home'),
                url(r'^finance/mortgage_calculator', views.mortgage_calculator,
                name='mortgage_calculator'),
              ]

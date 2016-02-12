"""launch_pad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from launch_pad import views
from finance import urls as finance_urls
from difference import urls as difference_urls
from fuel_price import urls as fuel_price_urls
from word_generator import urls as word_generator_urls
import autocomplete_light.shortcuts as al
al.autodiscover()
# import every app/autocomplete_light_registry.py
urlpatterns = [
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^about', views.about, name = 'about'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^', include(finance_urls)),
    url(r'^', include(difference_urls)),
    url(r'^', include(fuel_price_urls)),
    url(r'^', include(word_generator_urls)),


    # url(r'^mortgage_calulator', include(finance_urls)),

]

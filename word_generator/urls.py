from django.conf.urls import url, include
from word_generator import views

# import autocomplete_light
# autocomplete_light.autodiscover()
urlpatterns = [
                url(r'^word_generator$', views.word_generator_home, name = 'word_generator_home'),
              ]

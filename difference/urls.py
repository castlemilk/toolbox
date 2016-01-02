from django.conf.urls import url
from difference import views
urlpatterns = [
                url(r'^difference$', views.list_tools, name = 'difference_home'),
                url(r'^difference/text_diff', views.text_diff,
                name='text_diff'),
              ]

from django.conf.urls import url
from difference import views
urlpatterns = [
                url(r'^difference$', views.list_tools, name = 'difference_home'),
                url(r'^difference/text_diff_simple', views.text_diff_simple,
                name='text_diff_simple'),
                url(r'^difference/text_diff_advanced', views.text_diff_advanced,
                name='text_diff_advanced'),
              ]

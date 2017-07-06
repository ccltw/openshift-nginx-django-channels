from django.conf.urls import url
from example.views import sample


urlpatterns = [
    url(r'^$', sample, name='sample')
]
# polls/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^(?P<normalized_name>[a-z]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<normalized_name>[a-z]+)/results/$', views.results, name='results'),
]
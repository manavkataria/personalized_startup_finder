"""startup_finder URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from core import views

urlpatterns = [
    url(r'^$', include('core.urls')),
    # url(r'^core/', include('core.urls')),
    url(r'^admin/', admin.site.urls),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^login/$', 'django_social_app.views.login'),
    url(r'^home/$', 'django_social_app.views.home'),
    url(r'^logout/$', 'django_social_app.views.logout'),
    url(r'^(?P<normalized_name>[a-z]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<normalized_name>[a-z]+)/results/$', views.results, name='results'),
    url(r'^connections/$', 'django_social_app.views.connections'),
    url(r'^get_access_token/$', 'django_social_app.views.get_access_token'),
]

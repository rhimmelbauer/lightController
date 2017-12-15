"""lightController URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from lights import views

urlpatterns = [
    url(r'^$', views.stats, name='home'),
    url(r'^stats', views.stats, name='stats'),
    url(r'^new_zone', views.new_zone, name='new_zone'),
    url(r'^dashboard', views.dashboard, name='dashboard'),
    url(r'^edit_bulb/(?P<pk>\d+)/$', views.edit_bulb, name='edit_bulb'),
    url(r'^control_zone', views.control_zone, name='control_zone'),
    url(r'^admin/', admin.site.urls),
]

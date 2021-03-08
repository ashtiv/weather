"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from weatherapp.views import  get_name,add,naaam,bnaaam
from django.urls import re_path
from django.views.static import serve
from . import settings
handler400 = 'weatherapp.views.handler400'
handler403 = 'weatherapp.views.handler403'
handler404 = 'weatherapp.views.handler404'
handler500 = 'weatherapp.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('weather/', get_name),
    path('know/', add),
    path('search/<str:x>/', naaam),
    path('search//', bnaaam),   
]
urlpatterns += [
  re_path(r'^static/(?:.*)$', serve, {'document_root': settings.STATIC_ROOT, })
]

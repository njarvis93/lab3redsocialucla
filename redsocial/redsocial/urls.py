"""redsocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^red/', include('red.urls', namespace='red')),
    #url(r'^usuarios/', include('usuarios.urls', namespace='usuarios')),
    #url(r'^$',login, include('red.urls', namespace='red'))

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

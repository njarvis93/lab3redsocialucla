from django.conf.urls import patterns, url
from .views import Login
from django.contrib.auth.views import logout

urlpatterns = [
   url(r'^$', Login.as_view(), name="login"),
   url(r'^salir$', logout, name="salir", kwargs={'next_page': '/'}),
]
from django.conf.urls import url
from .views import Login, signup
from django.contrib.auth.views import logout

urlpatterns = [
   url(r'^$', Login.as_view(), name="login"),
   url(r'^salir$', logout, name="salir", kwargs={'next_page': '/'}),
   url(r'^signup$', signup, name='signup'),
]
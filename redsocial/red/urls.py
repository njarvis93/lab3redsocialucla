from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsuarioList, UsuarioDetail, CanalDetail, CanalList, ActividadesList, PostDetail, PostList

urlpatterns = [
    url(r'^api_users', UsuarioList.as_view()),
    url(r'^user/(?P<pk>[a-z0-9]+)/', UsuarioDetail.as_view()),
    url(r'^canales/', CanalList.as_view()),
    url(r'^canal/(?P<pk>[0-9]+)/', CanalDetail.as_view()),
    url(r'^post/actividad/(?P<id_post>[0-9]+)/', ActividadesList.as_view()),
    url(r'^all_post/', PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/', PostDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
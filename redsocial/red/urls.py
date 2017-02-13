from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsuarioList, UsuarioDetail, CanalDetail, CanalList, ActividadesList, PostDetail, PostList,\
    ActividadDetail, ComentariosList, AreaConocimientoList, AreaConocimientoDetail, ExperienciaLaboralDetail, ExperienciaLaboralList, \
    IdiomasList, IdiomasDetail, IdiomasPorUsuarioList, IdiomaPorUsuarioDetail, PerfilUserList, PerfilUserDetail, UserList, NivelFormacionList, \
    NivelFormacionDetail

urlpatterns = [
    url(r'^api_users', UsuarioList.as_view()),
    url(r'^user/(?P<pk>[a-z0-9]+)/', UsuarioDetail.as_view()),
    url(r'^canales/', CanalList.as_view()),
    url(r'^canal/(?P<pk>[0-9]+)/', CanalDetail.as_view()),
    url(r'^post/actividad/(?P<id_post>[0-9]+)/', ActividadesList.as_view()),
    url(r'^all_post/', PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/', PostDetail.as_view()),
    url(r'^actividad_por_post/(?P<id_post>[0-9]+)/(?P<tipo>[0-9]+)/$', ActividadDetail.as_view()),
    url(r'^comentarios_por_post/(?P<id_post>[0-9]+)/$', ComentariosList.as_view()),
    url(r'^areas_conocimiento/all', AreaConocimientoList.as_view()),
    url(r'^areas_conocimiento/(?P<pk>[0-9]+)/$', AreaConocimientoDetail.as_view()),
    url(r'^laboral/experiencias/usuario/(?P<id>[a-z0-9]+)/', ExperienciaLaboralList.as_view()),
    url(r'^laboral/usuario/(?P<id_autor>[a-z0-9]+)/experiencia_id/(?P<id>[0-9]+)/', ExperienciaLaboralDetail.as_view()),
    url(r'^idiomas/$', IdiomasList.as_view()),
    url(r'^idiomas/(?P<pk>[0-9]+)/$', IdiomasDetail.as_view()),
    url(r'^idiomas/usuario/(?P<perfil>[a-z0-9]+)/', IdiomasPorUsuarioList.as_view()),
    url(r'^idiomas/usuario/(?P<perfil>[a-z0-9]+)/(?P<idioma>[0-9]+)/$', IdiomaPorUsuarioDetail.as_view()),
    url(r'^user/profiles/', PerfilUserList.as_view()),
    url(r'^user/my_profile/(?P<pk>[a-z0-9]+)/$', PerfilUserDetail.as_view()),
    url(r'^todos/', UserList.as_view()),
    url(r'^formacion/user/(?P<id_autor>[a-z0-9]+)/$', NivelFormacionList.as_view()),
    url(r'^formacion/(?P<pk>[0-9]+)/user/(?P<id_autor>[a-z0-9]+)/$', NivelFormacionDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
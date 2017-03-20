from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UsuarioList, UsuarioDetail, CanalDetail, CanalList, ActividadesList, PostDetail, PostList,\
    ActividadDetail, ComentariosList, AreaConocimientoList, AreaConocimientoDetail, ExperienciaLaboralDetail, ExperienciaLaboralList, \
    IdiomasList, IdiomasDetail, IdiomasPorUsuarioList, IdiomaPorUsuarioDetail, PerfilUserList, PerfilUserDetail, UserList, NivelFormacionList, \
    NivelFormacionDetail, administrador, index, panel2, canales, panel3, panel4, canal, crearcanal, buscar, perfil, miperfil, timeline, \
    olvide, timeline_privado, config

urlpatterns = [
    url(r'^api_users', UsuarioList.as_view()), # Create-Read, Todos los usuarios
    url(r'^user/(?P<pk>[a-z0-9]+)/', UsuarioDetail.as_view()), #Update-Delete, Leer, Actualizar y borrar un usuario
    url(r'^canales/', CanalList.as_view()), # Create-Read para todos los canales
    url(r'^canal/(?P<pk>[0-9]+)/', CanalDetail.as_view()), #Update-.Delete por Canal
    url(r'^post/actividad/(?P<id_post>[0-9]+)/', ActividadesList.as_view()), #Create-Read, Actividad buscada con un id particular
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
    url(r'^formacion/(?P<pk>[0-9]+)/user/(?P<id_autor>[a-z0-9]+)/$', NivelFormacionDetail.as_view()), ##Hasta aqui las API
    url(r'^$', index, name='index'), ##Login
    url(r'^canalprincipal/$', canal, name='url_canalprincipal'), ##Canal
    url(r'^crearcanal/$', crearcanal, name='url_crearcanal'), ##Crear un canal
    url(r'^miperfil/$', miperfil, name='url_miperfil'), ##Mi perfil
    url(r'^perfil/$', perfil, name='url_perfil'), ##Perfil externo, ajeno al usuario logueado
    url(r'^timeline/$', timeline, name='url_timeline'), ## Muro
    url(r'^olvidemicontrasena/$', olvide, name='url_olvide'), ## Olvide mi contraseña
    url(r'^buscar/$', buscar, name='url_buscar'), ##Buscar
    url(r'^administrador/$', administrador, name='administrador'), ##Perfil del administrador de la red
    url(r'^panel_admin2/$', panel2, name='panelAd2'),
    url(r'^panel_admin3/$', panel3, name='panelAd3'),
    url(r'^panel_admin4/$', panel4, name='panelAd4'),
    url(r'^mis_canales/$', canales, name='canales_user'),
    url(r'^timeline_privado/$', timeline_privado, name='timeline_privado'),
    url(r'^config/$', config, name='config'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
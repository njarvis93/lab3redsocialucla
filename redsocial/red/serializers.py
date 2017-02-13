from rest_framework.serializers import ModelSerializer
from .models import Usuario, AreaConocimiento, Canal, Actividad, Comentario, Compartir, Post, Likes, ExperienciaLaboral, \
    Perfil, Interes, Idioma, NivelFormacion



class AreaConocimientoSerializer(ModelSerializer):

    class Meta:
        model = AreaConocimiento
        fields = ('nombre', 'descripcion')

class ExperienciaLaboralSerializer(ModelSerializer):

    class Meta:
        model = ExperienciaLaboral
        fields = ('id', 'empresa', 'cargo', 'fecha_inicio', 'fecha_fin', 'descripcion', 'id_autor')

class IdiomaSerializer(ModelSerializer):

    class Meta:
        model = Idioma
        fields = ('id', 'nombre', 'nivel')

class NivelFormacionSerializer(ModelSerializer):

    class Meta:
        model = NivelFormacion
        fields = ('id', 'institucion', 'titulo', 'competencias_adquiridas', 'fecha_inicio', 'fecha_finalizacion', 'tipo_formacion', 'nivel_educativo')

class InteresesSerializer(ModelSerializer):

    class Meta:
        model = Interes
        fields = ('id', 'descripcion')


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = (
        'username', 'email', 'nombres', 'apellidos', 'fecha_nacimiento', 'direccion', 'telefono_fijo', 'telefono_movil', 'telefono_oficina')


class PerfilSerializer(ModelSerializer):
    username = UsuarioSerializer(many=False, read_only=True)
    areas = AreaConocimientoSerializer(many=True, read_only=True)
    idiomas = IdiomaSerializer(many=True, read_only=True)
    intereses = InteresesSerializer(many=True, read_only=True)
    formacion = NivelFormacionSerializer(many=True)
    experiencia = ExperienciaLaboralSerializer(many=True)

    class Meta:
        model = Perfil
        fields = ('username', 'foto_perfil', 'url_facebook_perfil', 'url_twitter_perfil', 'areas', 'idiomas', 'intereses', 'formacion', 'experiencia')


class CompartirSerializer(ModelSerializer):
    autor = UsuarioSerializer(many=False)

    class Meta:
        model = Compartir
        fields = ('id', 'tipo', 'visibilidad', 'fecha_ocurrencia', 'autor', 'id_actividad')


class LikesSerializer(ModelSerializer):
    autor = UsuarioSerializer(many=False)

    class Meta:
        model = Likes
        fields = ('id', 'autor', 'fecha_ocurrencia', 'hora_ocurrencia', 'id_actividad')

class RespuestasComentariosSerializer(ModelSerializer):

    class Meta:
        model = Comentario
        fields = ('id', 'contenido', 'id_actividad', 'id_comentario_padre', 'fecha_ocurrencia', 'autor')

class ComentarioSerializer(ModelSerializer):
    autor = UsuarioSerializer(many=False)
    respuestas = RespuestasComentariosSerializer(many=True, read_only=True)

    class Meta:
        model = Comentario
        fields = ('id','contenido', 'id_actividad', 'id_comentario_padre', 'fecha_ocurrencia', 'autor', 'respuestas')
        ordering = ('-fecha_ocurrencia',)

class ActividadSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)
    shares = CompartirSerializer(many=True, read_only=True)
    me_gustas = LikesSerializer(many=True, read_only=True)

    class Meta:
        model = Actividad
        fields = ('id', 'id_post', 'tipo', 'comentarios', 'shares', 'me_gustas')
        ordering = 'tipo'

class PostSerializer(ModelSerializer):
    autor = UsuarioSerializer(many=False)
    actividad = ActividadSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'autor', 'contenido', 'fecha_creacion', 'hora_creacion', 'imagenes', 'audio', 'video', 'actividad')
        ordering = ('-fecha_creacion',)

class CanalSerializer(ModelSerializer):
    areas = AreaConocimientoSerializer(many=True, read_only=True)
    autor = UsuarioSerializer(many=False)
    posts = PostSerializer(many=True)

    class Meta:
        model = Canal
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'autor', 'areas', 'posts')


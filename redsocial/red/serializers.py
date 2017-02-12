from rest_framework.serializers import ModelSerializer
from .models import Usuario, AreaConocimiento, Canal, Actividad, Comentario, Compartir, Post, Likes

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombres', 'apellidos', 'fecha_nacimiento')

class AreaConocimientoSerializer(ModelSerializer):

    class Meta:
        model = AreaConocimiento
        fields = ('nombre', 'descripcion')


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

class CanalSerializer(ModelSerializer):
    areas = AreaConocimientoSerializer(many=True, read_only=True)
    autor = UsuarioSerializer(many=False)
    posts = PostSerializer(many=True)

    class Meta:
        model = Canal
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'autor', 'areas', 'posts')
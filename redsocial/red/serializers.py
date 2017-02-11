from rest_framework.serializers import ModelSerializer
from .models import Usuario, AreaConocimiento, Canal, Actividad, Comentario, Compartir, Post

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombres', 'apellidos', 'fecha_nacimiento')

class AreaConocimientoSerializer(ModelSerializer):

    class Meta:
        model = AreaConocimiento
        fields = ('nombre', 'descripcion')


class ComentarioSerializer(ModelSerializer):
    autor = UsuarioSerializer(many=False)

    class Meta:
        model = Comentario
        fields = ('contenido', 'id_actividad', 'id_comentario_padre', 'fecha_ocurrencia', 'autor')

class ActividadSerializer(ModelSerializer):
    comentarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Actividad
        fields = ('id', 'id_post', 'tipo', 'comentarios')
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
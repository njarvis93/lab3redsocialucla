from rest_framework.serializers import ModelSerializer
from .models import Usuario, AreaConocimiento, Canal

class UsuarioSerializer(ModelSerializer):

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'nombres', 'apellidos', 'fecha_nacimiento')

class AreaConocimientoSerializer(ModelSerializer):

    class Meta:
        model = AreaConocimiento
        fields = ('nombre', 'descripcion')

class CanalSerializer(ModelSerializer):
    areas = AreaConocimientoSerializer(many=True, read_only=True)
    autor = UsuarioSerializer(many=False)


    class Meta:
        model = Canal
        fields = ('nombre', 'descripcion', 'fecha_creacion', 'autor', 'areas')


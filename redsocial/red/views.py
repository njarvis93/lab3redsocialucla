import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from .models import Usuario, Canal, Post, Actividad, Comentario, AreaConocimiento, Perfil, Interes, Idioma, NivelFormacion, ExperienciaLaboral
from .serializers import UsuarioSerializer, AreaConocimientoSerializer, CanalSerializer, ActividadSerializer, ComentarioSerializer, PostSerializer, \
    PerfilSerializer, ExperienciaLaboralSerializer, IdiomaSerializer, InteresesSerializer, NivelFormacionSerializer
from django.shortcuts import render


# Create your views here.

class UsuarioList(APIView):
    """
    Lista de todos los usuarios, o crear un nuevo usuario
    """
    def get(self, request, format=None):
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioDetail(APIView):
    """
    Recuperar, actualizar o borrar una instancia de Usuario
    """
    def get_object(self, pk):
        try:
            return Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usuario = self.get_object(pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        usuario = self.get_object(pk)
        usuario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CanalList(generics.ListCreateAPIView):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer

class CanalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer


class ActividadesList(APIView):

   def get(self, request, id_post, format = None):
       actividad = Actividad.objects.filter(id_post=id_post)
       serializer = ActividadSerializer(actividad, many=True)
       return Response(serializer.data)

class ActividadDetail(APIView):

    def get_object(self, id_post, tipo):
        try:
            return Actividad.objects.get(id_post=id_post, tipo=tipo)
        except Actividad.DoesNotExist:
            raise Http404

    def get(self, request, id_post, tipo, format = None):
        actividad = self.get_object(tipo, id_post)
        serializer = ActividadSerializer(actividad)
        return Response(serializer.data)


class ComentariosList(APIView):

    def get_actividad(self, id_post, format=None):
        try:
            return Actividad.objects.get(id_post=id_post, tipo=1)
        except Actividad.DoesNotExist:
            raise Http404

    def get(self, request, id_post, format = None):
        actividad = self.get_actividad(id_post)
        comentario = Comentario.objects.filter(id_actividad=actividad.pk)
        serializer = ComentarioSerializer(comentario, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ComentarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComentarioDetail(APIView):
    """
    Recuperar, actualizar o borrar una instancia de Comentario
    """
    def get_object(self, pk):
        try:
            return Comentario.objects.get(idioma=pk)
        except Comentario.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comentario = self.get_object(pk)
        serializer = ComentarioSerializer(comentario)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comentario = self.get_object(pk)
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):
        comentario = self.get_object(pk)
        comentario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class AreaConocimientoList(generics.ListCreateAPIView):
    queryset = AreaConocimiento.objects.all()
    serializer_class = AreaConocimientoSerializer

class AreaConocimientoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AreaConocimiento.objects.all()
    serializer_class = AreaConocimientoSerializer

class ExperienciaLaboralList(APIView):

    def get_user(self, id):
        try:
            return Usuario.objects.get(pk=id)
        except Usuario.DoesNotExist:
            raise Http404

    def get(self, request, id, format = None):
        perfil = self.get_user(id)
        experiencia = ExperienciaLaboral.objects.filter(id_autor=perfil.pk)
        serializer = ExperienciaLaboralSerializer(experiencia, many=True)
        return Response(serializer.data)

    def post(self, request, id, format = None):
        serializer = ExperienciaLaboralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperienciaLaboralDetail(APIView):

    def get_object(self, id, id_autor):
        try:
            return ExperienciaLaboral.objects.get(pk=id, id_autor=id_autor)
        except ExperienciaLaboral.DoesNotExist:
            raise Http404

    def get(self, request, id_autor, id, format = None):
        experiencia = self.get_object(id, id_autor)
        serializer = ExperienciaLaboralSerializer(experiencia)
        return Response(serializer.data)

    def put(self, request, id, id_autor, format=None):
        experiencia = self.get_object(id, id_autor)
        serializer = ExperienciaLaboralSerializer(experiencia, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, id_autor, format=None):
        experiencia = self.get_object(id, id_autor)
        experiencia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IdiomasList(generics.ListCreateAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class IdiomasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class IdiomasPorUsuarioList(APIView):

    def get(self, request, perfil, format=None):
        idiomas = Idioma.objects.filter(perfil=perfil)
        serializer = IdiomaSerializer(idiomas, many=True)
        return Response(serializer.data)

    def post(self, request, perfil, format=None):
        serializer = IdiomaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IdiomaPorUsuarioDetail(APIView):

    def get_object(self, perfil, idioma):
        try:
            return Idioma.objects.get(perfil=perfil, id=idioma)
        except Idioma.DoesNotExist:
            raise Http404

    def get(self, request, perfil, idioma, format=None):
        idioma = self.get_object(perfil, idioma)
        serializer = IdiomaSerializer(idioma)
        return Response(serializer.data)

    def put(self, request, perfil, idioma, format=None):
        idioma = self.get_object(perfil, idioma)
        serializer = IdiomaSerializer(idioma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, perfil, idioma, format=None):
        idioma = self.get_object(perfil, idioma)
        idioma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PerfilUserList(generics.ListCreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class PerfilUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class UserList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class NivelFormacionList(APIView):
    def get(self, request, id_autor, format=None):
        formaciones = NivelFormacion.objects.filter(id_autor=id_autor)
        serializer = NivelFormacionSerializer(formaciones, many=True)
        return Response(serializer.data)

    def post(self, request, id_autor, format=None):
        serializer = NivelFormacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NivelFormacionDetail(APIView):

    def get_object(self, id_autor, pk):
        try:
            return NivelFormacion.objects.get(pk=pk, id_autor=id_autor)
        except NivelFormacion.DoesNotExist:
            raise Http404

    def get(self, request, id_autor, pk, format=None):
        formacion = self.get_object(id_autor, pk)
        serializer = NivelFormacionSerializer(formacion)
        return Response(serializer.data)

    def put(self, request, id_autor, pk, format=None):
        formacion = self.get_object(id_autor, pk)
        serializer = IdiomaSerializer(formacion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_autor, pk, format=None):
        formacion = self.get_object(id_autor, pk)
        formacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, 'redtem/integrantescanal.html')

def home(request):
    return render(request, 'redtem/timline.html')

def canales(request):
    return render(request, 'redtem/canal.html')

def administrador(request):
    return render(request, 'redtem/panel_admin1.html')

def panel2(request):
    return render(request, 'redtem/panel_admin2.html')
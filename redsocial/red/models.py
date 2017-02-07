#Integrantes:
#NARVIS GIL, CI. 20923170
#EVELYN PUERTA, CI. 20921080
#GLENNISBETH RODRIGUEZ, CI. 21506603
#MIGDALIA ATACHO, CI 23484707

#SECCION 01

from django.contrib.postgres.fields import ArrayField
from django.db import models


# Create your models here.

def user_directory_path_audio(instance, filename):
    return 'user_{0}/audio/%Y/%m/%d/{1}'.format(instance.user.id, filename)


def user_directory_path_images(instance, filename):
    return 'user_{0}/images/%Y/%m/%d/{1}'.format(instance.user.id, filename)


def user_directory_path_videos(instance, filename):
    return 'user_{0}/videos/%Y/%m/%d/{1}'.format(instance.user.id, filename)


def user_directory_profile_picture(instance, filename):
    return 'user_{0}/profile_pic/%Y/%m/%d/{1}'.format(instance.user.id, filename)


class Permiso(models.Model):
    descripcion = models.CharField(max_length=30)


class Rol(models.Model):
    nombres = models.CharField(max_length=254)
    descripcion = models.TextField()
    permisos = models.ManyToManyField(Permiso)


class AreaConocimiento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Idioma(models.Model):
    nombre = models.CharField(max_length=20)
    nivel = models.IntegerField()

class Usuario(models.Model):
    username = models.CharField(max_length=15, primary_key=True, unique=True)
    password = models.TextField()
    roles = models.ManyToManyField(Rol)
    email = models.EmailField(max_length=254, unique=True)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=300)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField()
    telefono_movil= models.CharField(max_length=20)
    telefono_fijo = models.CharField(max_length=20)
    telefono_oficina = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % self.nombres+' '+self.apellidos

class Seguidor(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estatus = models.IntegerField()
    fecha_actividad = models.DateField()

class Perfil(models.Model):
    id = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    intereses = ArrayField(ArrayField(models.TextField()))
    areas = models.ManyToManyField(AreaConocimiento)
    idiomas = models.ManyToManyField(Idioma)
    seguidores = models.ManyToManyField(Seguidor, blank=True)
    #siguiendo = models.ManyToManyField(Usuario, blank=True)
    foto_perfil = models.ImageField(upload_to=user_directory_profile_picture)
    url_facebook_perfil = models.URLField()
    url_twitter_perfil = models.URLField()

class NivelFormacion(models.Model):
    institucion = models.CharField(max_length=100)
    titulo_obtenido = models.CharField(max_length=30)
    competencias_adquiridas = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    tipo_formacion = models.IntegerField()
    nivel_educativo = models.IntegerField()
    id_autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Canal(models.Model):
    nombre = models.TextField(max_length=20)
    descripcion = models.TextField(max_length=100)
    fecha_creacion = models.DateTimeField()
    autor = models.ForeignKey(Usuario, related_name='autor', on_delete=models.CASCADE, unique=True)
    areas = models.ManyToManyField(AreaConocimiento, related_name='areas')
    miembros = models.ManyToManyField(Perfil)

class Post(models.Model):
    tipo = models.IntegerField()
    autor = models.ForeignKey(Usuario)
    contenido = models.TextField()
    imagenes = models.ImageField(upload_to=user_directory_path_images)
    audio = models.FileField(upload_to=user_directory_path_audio)
    video = models.FileField(upload_to=user_directory_path_videos)
    fecha_creacion = models.DateField()
    hora_creacion = models.TimeField()
    id_canal = models.ManyToManyField(Canal, blank=True)

class Actividad(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor_actividad = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_ocurrencia = models.DateField()
    hora_ocurrencia = models.TimeField()
    tipo = models.IntegerField()


class Comentario(models.Model):
    contenido = models.TextField()
    tipo = models.IntegerField()
    id_comentario_padre = models.ForeignKey('self', related_name='lista_respuesta', null=True)
    id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

class ExperienciaLaboral(models.Model):
    empresa = models.CharField(max_length=50)
    cargo = models.CharField(max_length=30)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    id_autor = models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Compartir(models.Model):
    tipo = models.IntegerField()
    visibilidad = models.IntegerField()
    id_actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)

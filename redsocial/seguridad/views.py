from django.shortcuts import render
# Importamos la vista genérica FormView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
# Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import FormularioLogin
#--------------------------
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from .forms import SignUpForm

# Create your views here.
class Login(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'redtem/login.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = FormularioLogin
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy("red:url_timeline")

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            return HttpResponseRedirect(reverse_lazy("seguridad:login"))
    else:
        form = SignUpForm()

    data = {
        'form': form,
    }
    return render_to_response('redtem/signup.html', data, context_instance=RequestContext(request))
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from django.contrib.auth import login, authenticate, logout

# importamos sistema de mensajes de Django
from django.contrib import messages
from .forms import RegisterForm, LoginForm


class IndexView(TemplateView):
    template_name = 'index.html'


# class RegisterView(View):
#     def get(self, request):
#         template_name = 'register.html'
#         return render(request, template_name)
#
#     def post(self, request):
#         data = request.POST
#         post_username = data.get('username', None)
#         password = data.get('password', None)
#         password2 = data.get('password-confirmation', None)
#         # Utilizamos el método filter para filtrar los usuarios que tengan el mismo username
#         # que el username que viene en el post method
#         # Agregamos el método .exists() al final para que nos responda con un True o False
#         # si es que encontro o no encontro registros
#
#         if User.objects.filter(username=post_username).exists():
#             messages.error(request, 'Lo sentimos este nombre de usuario ya fue utilizado. Ingresa otro.')
#             return redirect('user-register')
#
#         if not password == password2:
#             messages.error(request, 'Lo sentimos las contraseñas no son iguales.')
#             return redirect('user-register')
#
#         else:
#             user = User.objects.create(
#                 username=data['username'],
#                 email=data['email'],
#                 password=data['password']
#             )
#             messages.success(request, 'Se ha creado tu usuario con éxito!')
#             return redirect('home')


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        template_name = 'register.html'
        return render(request, template_name, dict(form=RegisterForm()))

    def post(self, request):
        template_name = 'register.html'
        data = request.POST
        form = RegisterForm(data)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save()
            login(request, user)
            messages.success(request, 'Registro con éxito')
            return redirect('home')
        else:
            messages.error(request, 'Ingresaste datos incorrectos. Revisalos.')
            for field in form.errors:
                form.fields[field].widget.attrs['class'] = 'input is-danger'
            return render(request, template_name, dict(form=form))


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = LoginForm()
            return render(request, self.template_name, dict(form=form))

    def post(self, request):
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        messages.error(request, 'El usuario o contraseña estan incorrectos')
        return render(request, self.template_name, dict(form=form))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

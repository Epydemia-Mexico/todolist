"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Se importa la configuracion para que django pueda servir los archivos MEDIA.
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (
    IndexView,
    RegisterView,
    LoginView,
    LogoutView,
)

from todo.views import TodoCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='home'),
    path('registro', RegisterView.as_view(), name='user-register'),
    path('inicia-sesion', LoginView.as_view(), name='user-login'),
    path('cierra-sesion', LogoutView.as_view(), name='user-logout'),
    path('crear-tarea', TodoCreateView.as_view(), name='create-todo'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Se agrega la ruta donde estara nuestra carpeta Media en un entorno de desarollo.



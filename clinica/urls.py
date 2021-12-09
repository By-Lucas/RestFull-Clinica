"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from  rest_framework import routers

from  pacientes.api.viewsets import Pacientes_viewsets
from agendamentos.api.viewsets import Agendamentos_viewsets
from historicos.api.viewsets import Historicos_viresets
# ROTAS
router = routers.DefaultRouter()
router.register(r'pacientes', Pacientes_viewsets)
router.register(r'agendamentos', Agendamentos_viewsets)
router.register(r'historicos', Historicos_viresets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

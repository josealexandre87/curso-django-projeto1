"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# Para servir as medias na pasta recipe/cover e 
# importar os arquivos estáticos nas urls temos que importar os seguintes módulos:
from django.conf.urls.static import static
from django.conf import settings # importando do arquivo settings.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), # dominio/recipes/<o path que estiver em recipes.urls>/
]
# Temos que concatenar as urlspaterns!
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# Statics é uma função que passa o prefixo da url e indica onde estão as medias
# e os arquivos estáticos para serem servidos ao usuário. 
# Ele recebe o prefixo definidos em settings.py           
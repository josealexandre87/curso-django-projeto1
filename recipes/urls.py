from django.urls import path
from recipes.views import home

# dominio/recipes/<PATH> ---- exemplo dominio/recipes/home/
urlpatterns = [
    path('', home), # /home/
]

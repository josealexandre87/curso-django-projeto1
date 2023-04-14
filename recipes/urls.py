from django.urls import path
# from recipes.views import home   **não foi preciso importar o home, pois precisarei importar muitas urls.
from . import views     # **então, vamos importar da pasta que estou "." o módulo todo "views" que renderiza as URLS!!!

# dominio/recipes/<PATH> ---- exemplo dominio/recipes/home/
urlpatterns = [
    path('', views.home), # agora preciso importar do módulo "views" usando "." dotnotation!! -> antes era só path('', home),
    path('recipes/<int:id>/', views.recipe), # recipes/ é de onde eu quero que começe a URL recipe. Ficará: recipes/recipe/
]          # int:id (só aceita inteiros)    # e o Django precisa colocar <parâmetro>/ para receber um argumento da página que 
                                            # a minha view vai renderizar (views.recipe). ! <ID>/ será parâmetro da minha VIEWS !
                                            # Temos que ir na função recipe(request) em views.py, e passar esse novo parâmetro 
                                            # <id> para a função!

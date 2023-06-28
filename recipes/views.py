from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# faz uma requisição e renderiza no servidor a resposta do documento html em 'recipes/pages/home.html'. 
# é uma função de renderização
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={  
        'recipes': [make_recipe() for _ in range(10)], # pode criar variáveis que serão usadas no corpo do hmtl chamando {{name}} e renderizados na página
    })

def recipe(request, id): # COPIADA E MUDADA O NOME PARA 'recipe', deve ser inserida em urlpatterns =[], no arquivo recipes/urls.py
    return render(request, 'recipes/pages/recipe-view.html', context={  
        'recipe': make_recipe(), # pode criar variáveis que serão usadas no corpo do hmtl chamando {{name}} e renderizados na página
        'is_detail_page': True, # foi criada a variável is_detail_page = True para que seja usada como condicional no arquivo 
                                # partials/recipe.html sendo renderizada ou não, dependendo do seu estado atual. E foram criados dois blocos
                                # {%if%} e {%endif%} para controle da div <footer>.
    })
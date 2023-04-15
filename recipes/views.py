from django.shortcuts import render
from utils.recipes.factory import make_recipe

# faz uma requisição e renderiza no servidor a resposta do documento html em 'recipes/pages/home.html'. 
# é uma função de renderização
def home(request):
    return render(request, 'recipes/pages/home.html', context={  
        'recipes': [make_recipe() for _ in range(10)], # pode criar variáveis que serão usadas no corpo do hmtl chamando {{name}} e renderizados na página
    })

def recipe(request, id): # COPIADA E MUDADA O NOME PARA 'recipe', deve ser inserida em urlpatterns =[], no arquivo recipes/urls.py
    return render(request, 'recipes/pages/recipe-view.html', context={  
        'recipe': make_recipe(), # pode criar variáveis que serão usadas no corpo do hmtl chamando {{name}} e renderizados na página
    })
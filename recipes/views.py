from django.shortcuts import render

# faz uma requisição e renderiza no servidor a resposta do documento html em 'recipes/pages/home.html'. 
# é uma função de renderização
def home(request):
    return render(request, 'recipes/pages/home.html', context={  
        'name': '', # pode criar variáveis que serão usadas no corpo do hmtl chamando {{name}} e renderizados na página
    })
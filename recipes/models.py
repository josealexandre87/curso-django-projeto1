from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# MODELS SÃO a forma do Django se comunicar com o Banco de Dados.
# Ele usa o CRUD e tbm as sintaxes de SQL e NoSQL.
# Resumindo é uma forma diferente, talvez um pouco mais complicada, de interagir com o DB.

# LEMBRAR de SEMPRE usar models.XXXXX para utilizar as classes de django.db -> models
class Category(models.Model):
    name = models.CharField(max_length=65)
    def __str__(self): # é um metodo que faz com que o admin.py mude o nome da class na página do admin e apareça o nome do própio modelo criado.
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=65) #(1)* VAI SER O NOME DO OBJETO lá no Admin
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
        )
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
        )
    
    def __str__(self): # é um metodo que faz com que o admin.py mude o nome da class na página do admin e apareça o nome do própio modelo criado.
        return self.title # * title VAI SER O NOME DO OBJETO lá no Admin
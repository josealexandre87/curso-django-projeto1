from django.contrib import admin
from .models import Category
from .models import Recipe

# Register your models here.
# tem que regisrar os models para que ele apareça na área de admin do Django. .../admin/
class CategoryAdmin(admin.ModelAdmin): 
    ...
admin.site.register(Category, CategoryAdmin) # passar o parâmetros(model importado do arquivo models.py="Category", class inserida='CategoryAdmin)
@admin.register(Recipe) # podemos usar tbm o decorator @admin.register para registrar o model
class RecipeAdmin(admin.ModelAdmin):
    ...




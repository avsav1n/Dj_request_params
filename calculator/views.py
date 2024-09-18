from django.conf import settings
from django.shortcuts import render
from django.urls import reverse

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    pages = {
        f'Рецепт {recipe}': reverse(recipe) for recipe in settings.DATA
    }
    context = {
        'pages': pages
    }
    return render(request, r'calculator/home.html', context)

def recipe_view(request):
    servings = request.GET.get('servings', 1)
    recipe = request.path_info.lstrip('/')
    context = {
        'name': f'Ингредиенты для {recipe}, порций - {servings}',
        'recipe': {
            ingredient.capitalize(): round(quantity * int(servings), 2) 
            for ingredient, quantity in settings.DATA[recipe].items()
        }
    }
    return render(request, r'calculator\index.html', context)


from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/recipe.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/index.html'
    recipes = DATA.keys()
    # for recipe in recipes():
    #     print(recipe)
    context = {"recipes": recipes}
    return render(request, template_name, context)

def recipe_omlet(request):
    template_name = 'calculator/recipe.html'
    context = {"recipe": DATA.get("omlet")}
    return render(request, template_name, context)

def recipe(request, recipe):
    template_name = 'calculator/recipe.html'
    servings = int(request.GET.get('servings', 1))
    if DATA.get(recipe):
        context = {recipe: DATA.get(recipe)}
        for recipe, ingr in context.items():
            for product, gr in ingr.items():
                ingr[product] = float(gr) * servings
            context = {recipe: ingr}
    else:
        context = {}
    return render(request, template_name, {'recipe': context})

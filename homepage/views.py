from django.shortcuts import render
from .models import Recipe, Author


def index(request):
    recipes_list = Recipe.objects.all()
    return render(request, "index.html",
                  {"data": recipes_list, "title": "Recipe Box"})


def recipeDetail(request, recipe_id):
    recipe_detail = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html",
                  {"recipe": recipe_detail})


def authorDetail(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    recipes = Recipe.objects.filter(author=author_id)
    return render(request, "author_detail.html",
                  {"recipes": recipes, "author": author})

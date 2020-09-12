"""recipe_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage.views import index, recipeDetail, authorDetail, addrecipe, addauthor, login_view, logout_view, signup, EditRecipeView, add_fav

urlpatterns = [
    path('', index, name = "homepage"),
    path('recipe/<int:recipe_id>/', recipeDetail),
    path('author/<int:author_id>/', authorDetail),
    path("addrecipe/", addrecipe),
    path("addauthor/", addauthor),
    path('addFavorite/<int:post_id>/', add_fav),
    path('editRecipe/<int:post_id>/', EditRecipeView.as_view()),
    path("login/", login_view),
    path("logout/", logout_view),
    path("signup/", signup),
    path('admin/', admin.site.urls),
]

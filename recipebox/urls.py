"""recipebox URL Configuration

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
from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipe/<int:post_id>/', views.post_detail),
    path('newrecipe/', views.recipe_form, name="newrecipe"),
    path('newauthor/', views.author_form, name='newauthor'),
    path("author/<int:id>/", views.recipe_list),
    path('editRecipe/<int:post_id>/', views.EditRecipeView.as_view()),
    path('addFavorite/<int:post_id>/', views.add_favorite),
    path("login/", views.user_login, name="userlogin"),
    path('logout/', views.user_logout, name="userlogout"),
    path('signup/', views.signup_view, name="usersignup"),
    path('admin/', admin.site.urls),
]

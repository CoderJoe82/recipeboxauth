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
from homepage.views import index, post_detail, recipe_list, recipe_form, author_form, user_login, user_logout, signup_view

urlpatterns = [
    path('', index, name = "homepage"),
    path('recipe/<int:post_id>/', post_detail),
    path('newrecipe/', recipe_form, name = "newrecipe"),
    path('newauthor/', author_form, name = 'newauthor'),
    path("author/<int:id>", recipe_list),
    path("login/", user_login, name = "userlogin"),
    path('logout/', user_logout, name = "userlogout"),
    path('signup/', signup_view, name = "usersignup"),
    path('admin/', admin.site.urls),
]

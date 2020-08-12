from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.forms import AddRecipe, AuthorForm, LoginForm, SignupForm
from homepage.models import Recipe, Author
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "welcome_name": "SE-9"})

def post_detail(request, post_id):
    my_recipe = Recipe.objects.filter(id=post_id).first()
    return render(request, "post_detail.html", {'post': my_recipe})

def recipe_list(request, id):
    authors = Author.objects.all().filter(id=id)
    items = Recipe.objects.all().filter(author_id=id)
    return render(request, "recipe_list.html", {'recipes': items, "authors": authors})

@login_required
def recipe_form(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data.get('title'),
                body = data.get('body'),
                author = request.user.author
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipe()
    return render(request, "recipe_and_author_forms.html", {"form": form})

@login_required
@staff_member_required
def author_form(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    form = AuthorForm()
    return render(request, "recipe_and_author_forms.html", {'form': form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username = data.get('username'), password = data.get('password'))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse("homepage"))
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = LoginForm()
    return render(request, "recipe_and_author_forms.html", {'form': form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username = data.get('username'), password = data.get('password'))
            Author.objects.create(name = data.get('username'), user = new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = SignupForm
    return render(request, "recipe_and_author_forms.html", {'form': form})

"""
localhost:8000/
localhost:8000/post/3
"""
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from .models import Recipe, Author, User
from .forms import RecipesForm, AuthorsForm, LoginForm, SignupForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    fav_list = []
    for rec in auhor.favorites.all():
        fav_list.append(rec.id)
    items = Reecipe.objects.all().filter(author_id = id)
    fav_rec = Recipe.objects.filter(id__in = fav_list)

    return render(request, 'author_detail.html', {'recipes': items, 'authors': author, 'fav_rec': fav_rec})

@login_required()
def addrecipe(request):
    html = "addrecipe.html"
    form = None
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data["title"],
                author=data["author"],
                description=data["description"],
                instructions=data["instructions"],
            )
        return render(request, "added.html")
    else:
        form = RecipesForm()
    return render(request, html, {"form": form})


@login_required()
@staff_member_required()
def addauthor(request):
    html = "addauthor.html"
    form = None
    if request.method == "POST":
        form = AuthorsForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
            )
        return render(request, "added.html")
    else:
        form = AuthorsForm()
    return render(request, html, {"form": form})

class EditRecipeView(LoginRequiredMixin, TemplateView):
    def get(self, request, post_id):
        recipe = Recipe.objects.get(id=post_id)
        data = {
            "title": recipe.title,
            "body": recipe.body
        }
        form = AddRecipe(initial=data)
        return render(request, "recipe_and_author_forms.html", {"form": form})

def post(self, request, post_id):
    recipe = Recipe.objects.get(id=post_id)
    form = AddRecipe(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        recipe.title = data.get("title")
        recipe.body = data.get("body")
        recipe.save()
        return HttpResponseRedirect(reverse("homepage"))


def signup(request):
    html = 'signup.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["password"])
            login(request, user)
            Author.objects.create(
                name=data["name"],
                bio=data["bio"],
                user=user
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = 'login.html'
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

def add_fav(request, post_id):
    recipe = Recipe.objects.get(id = post_id)
    request.user.auhtor.favorites.add(recipe)
    return redirect('/recipe/' + str(post_id) + '/')
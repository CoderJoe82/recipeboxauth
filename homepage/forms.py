from django import forms
from homepage.models import Recipe, Author

class AddRecipe(forms.Form):
    title = forms.CharField(max_length = 50)
    body = forms.CharField(widget = forms.Textarea)
    # author = forms.ModelChoiceField(queryset = Author.objects.all())

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 240)
    password = forms.CharField(widget = forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(max_length = 240)
    password = forms.CharField(widget = forms.PasswordInput)
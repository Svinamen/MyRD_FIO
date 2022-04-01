from django import forms
from django.forms import ModelForm
from .models import Author, Genre, Book

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields='__all__'

class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields='__all__'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields='__all__'
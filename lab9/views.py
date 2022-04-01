from django.http import HttpResponse
from django.shortcuts import render
from .models import Author, Genre, Book
from .forms import AuthorForm, GenreForm, BookForm
from scipy.optimize import linprog
from django.conf import settings
import numpy as np
import matplotlib.pyplot as plt
import os
from django.conf import settings
def home(request):
    return HttpResponse('<h1>Lab9 </h1>')
def renders(request):
    return render(request, 'lab9/Start.html', {"Author": Author.objects.all(), "Genre":Genre.objects.all(), "Book":Book.objects.all()})
def books_for_genre(request):
    g = request.POST['Genres']
    return render(request, 'lab9/books_for_genre.html',{'bo':Book.objects.filter(genre__name=g)})
def author_for_genres(request):
    a = request.POST['authors']
    return render(request, 'lab9/author_for_genres.html', {'at':Book.objects.filter(author__first_name=a)})
def index(request):
    form_A = AuthorForm()
    form_G = GenreForm()
    form_B = BookForm()
    try:
        if(request.POST['Author']):
            form_A = AuthorForm(request.POST)
    except:
        pass
    try:
        if (request.POST['Genre']):
            form_G = GenreForm(request.POST)
    except:
        pass
    try:
        if (request.POST['Book']):
            form_B = BookForm(request.POST)
    except:
        pass
    if(form_A.is_valid()):
        form_A.save()
    if (form_G.is_valid()):
        form_G.save()
    if (form_B.is_valid()):
        form_B.save()
    form_A = AuthorForm()
    form_G = GenreForm()
    form_B = BookForm()
    return render(request, 'lab9/index.html', {'form_A':form_A,'form_G':form_G,'form_B':form_B, })

def dates(request):
    array_year=[]
    size=Book.objects.all().count()
    for i in range(size):
        temp = str(Book.objects.all().values_list('year')[i][0])
        temp = int(temp[0:4])
        array_year.append(temp)
    array_year=sorted(array_year)
    array_book=[]
    for i in range(size):
        for j in range(size):
            temp = str(Book.objects.all().values_list('year')[j][0])
            temp = int(temp[0:4])
            print("temp ",temp)
            if array_year[i]==temp:
                array_book.append(str(Book.objects.all()[j]) )
                break




    return  render(request, 'lab9/sort_date.html', {'dd': array_book})




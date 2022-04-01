from django.db import models

class Author(models.Model):
    first_name=models.CharField('name_author',max_length=64)
    last_name=models.CharField('surname_author',max_length=64)
    birth_year=models.DateField('date_of_birth_author')

    def __str__(self):
        return f"{self.id}: {self.first_name}; {self.last_name}; {self.birth_year}"

class Genre(models.Model):
    name = models.CharField('name_genre',max_length=64)
    description = models.TextField('description_genre')

    def __str__(self):
        return f"{self.id}; {self.name}; {self.description}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='authors')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')
    name = models.CharField('name_book',max_length=100)
    year = models.DateField('year_book')
    pages = models.PositiveIntegerField('pages_book')

    def __str__(self):
        return f"{self.id}: {self.author},{self.genre},{self.name}; {self.year}; {self.pages}"






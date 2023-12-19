from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author , on_delete = models.CASCADE)
    publication_date = models.DateField()
    isbn = models.CharField(max_length= 13)
    available = models.BooleanField(default=True)




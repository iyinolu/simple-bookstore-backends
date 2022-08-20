from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Book(models.Model):
    name = models.CharField(max_length=100, blank=True)
    isbn = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="book")

    def __str__(self):
        return self.name

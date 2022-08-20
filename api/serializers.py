from dataclasses import field
from rest_framework import serializers
from api.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        field = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        field = ["name", "isbn", "author"]
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from api.serializers import BookSerializer, AuthorSerializer
from rest_framework.renderers import JSONRenderer
from api.models import Book, Author


class BookView(ListModelMixin,
               CreateModelMixin,
               GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]


class BookGetView(RetrieveUpdateAPIView, GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]


class AuthorView(ListModelMixin,
                 CreateModelMixin,
                 RetrieveModelMixin,
                 UpdateModelMixin,
                 GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]

class AuthorGetView(RetrieveUpdateAPIView, GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]

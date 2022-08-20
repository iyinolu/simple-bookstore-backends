from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from api.serializers import BookSerializer, AuthorSerializer
from rest_framework.renderers import JSONRenderer
from api.models import Book, Author


class BookView(ListCreateAPIView,
               GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]
    permission_classes = []


class BookGetView(RetrieveUpdateAPIView, GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    renderer_classes = [JSONRenderer]
    permission_classes = []


class AuthorView(ListCreateAPIView, GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    renderer_classes = [JSONRenderer]
    permission_classes = []


class AuthorGetView(RetrieveUpdateAPIView, GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    renderer_classes = [JSONRenderer]
    permission_classes = []

# 2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
from django.contrib import admin
from django.urls import path, include
from api.views import *

urlpatterns = [
    path('/book', BookView.as_view(), name="book"),
    path('/book/<int:pk>', BookGetView.as_view(), name="book-get"),
    path('/book', Author.as_view(), name="author"),
    path('/book/<int:pk>', AuthorGetView. as_view(), name="author-get"),
]
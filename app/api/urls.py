from django.urls import path
from .views import books_api,author_api

urlpatterns = [
    path('author/',author_api),
    path('books/',author_api),
]
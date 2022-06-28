from django.urls import path

from .views import viewAllAuthors,addNewAuthor,deleteAuthor,updateAuthor,editAuthor,viewAllBooks,detailBook,deleteBook,updateBook,editBook,createBook

urlpatterns = [
    path('authors/all/',viewAllAuthors,name='viewAllAuthors'),
    path('authors/add/',addNewAuthor,name='addNewAuthor'),
    path('authors/delete/<int:id>/',deleteAuthor,name='deleteAuthor'),
    path('author/edit/<int:id>/',editAuthor,name='editAuthor'),
    path('author/update/',updateAuthor,name='updateAuthor'),

    path('',viewAllBooks,name='viewAllBooks'),
    path('book/create/',createBook,name='createBook'),
    path('book/<int:id>/',detailBook,name='detailBook'),
    path('book/edit/<int:id>/',editBook,name='editBook'),
    path('book/update/',updateBook,name='updateBook'),
    path('book/delete/<int:id>/',deleteBook,name='deleteBook'),
]
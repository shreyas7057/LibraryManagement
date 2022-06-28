from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Author,Book


@login_required(login_url='login_user')
def viewAllAuthors(request):
    authors = Author.objects.all()
    context = {
        'authors':authors,
    }
    return render(request,'app/viewAuthors.html',context)


@login_required(login_url='login_user')
def addNewAuthor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        phone_num = request.POST.get('phone_num')
        author = Author(name=name,email_id=email_id,phone_num=phone_num)
        author.save()
        messages.success(request,'Author added successfully')
        return redirect('viewAllAuthors')
    
    return render(request,'app/addAuthor.html')


@login_required(login_url='login_user')
def editAuthor(request,id):
    author = Author.objects.get(id=id)

    context = {
        'author':author,
    }
    return render(request,'app/editAuthor.html',context)


@login_required(login_url='login_user')
def updateAuthor(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email_id = request.POST.get('email_id')
        phone_num = request.POST.get('phone_num')
        
        id = request.POST.get('id')

        author = Author.objects.get(id=id)
        author.name = name
        author.email_id = email_id
        author.phone_num = phone_num
        author.save()
        messages.success(request,'Author successfully updated!!')
        return redirect('viewAllAuthors')

    return render(request,'app/editAuthor.html')



@login_required(login_url='login_user')
def deleteAuthor(request,id):
    author = Author.objects.get(id=id)
    author.delete()
    messages.success(request,'Author Deleted Successfully')
    return redirect('viewAllAuthors')


login_required(login_url='login_user')
def createBook(request):
    author = Author.objects.all()
    if request.method=="POST":
        name = request.POST.get('name')  
        image = request.FILES.get('image')
        isbn_num = request.POST.get('isbn_num') 
        category = request.POST.get('category') 
        quantity = request.POST.get('quantity') 
        author = request.POST.get('author')

        author = Author.objects.get(id=author)

        book = Book(
            name = name,isbn_num=isbn_num,image=image,author=author,category=category,quantity=quantity
        )
        book.save()
        messages.success(request,'Books Details added!')
        return redirect('viewAllBooks')

    context = {
        'author':author
    }

    return render(request,'app/addBooks.html',context)


login_required(login_url='login_user')
def viewAllBooks(request):
    books = Book.objects.all()
    context = {
        'books':books
    }
    return render(request,'app/allBooks.html',context)


login_required(login_url='login_user')
def detailBook(request,id):
    book = Book.objects.get(id=id)
    context= {
        'book':book,
    }
    return render(request,'app/detailBook.html',context)


login_required(login_url='login_user')
def deleteBook(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request,'Successfully deleted book')
    return redirect('viewAllBooks')



@login_required(login_url='login_user')
def editBook(request,id):
    book = Book.objects.get(id=id)
    author = Author.objects.all()

    context = {
        'book':book,
        'author':author,
    }
    return render(request,'app/editBook.html',context)


@login_required(login_url='login_user')
def updateBook(request):
    if request.method == "POST":
        name = request.POST.get('name')
        isbn_num = request.POST.get('isbn_num')
        quantity = request.POST.get('quantity')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        author = request.POST.get('author')
        
        book_id = request.POST.get('id')

        book = Book.objects.get(id=book_id)
        book.name = name
        book.isbn_num = isbn_num
        book.quantity = quantity
        book.category = category
        book.image = image

        author = Author.objects.get(id=author)
        book.author = author

        if image !=None and  image != '':
            book.image = image
        
        if author !=None and author!='':
            book.author = author

        book.save()
        messages.success(request,'Book successfully updated!!')
        return redirect('viewAllBooks')

    return render(request,'app/editBook.html')
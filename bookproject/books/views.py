from django.shortcuts import render, redirect
from .models import Book
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    books=Book.objects.all()
    featured=books[:3]

    return render(request, 'books/home.html',{'featured':featured})

def book_list(request):
    books=Book.objects.all()

    return render(request, 'books/book_list.html',{'books':books})

def add_book(request):
    if request.method=='POST':
        title=request.POST.get('title')
        author=request.POST.get('author')
        category=request.POST.get('category')
        year=request.POST.get('year')

        Book.objects.create(
            title=title,
            author=author,
            category=category,
            year=year
        )
        return redirect('book_list')

    return render(request,'books/add_book.html')

def book_detail(request,id):
    book = get_object_or_404(Book, id=id)

    return render(request, 'books/book_detail.html', {'book': book})

def edit_book(request, id):
    book=get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.category = request.POST.get('category')
        book.year = request.POST.get('year')
        book.save()
        return redirect('book_list')
    return render(request, 'books/edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    
    return render(request, 'books/delete_book.html', {'book': book})

def about(request):
    return render(request, 'books/about.html')
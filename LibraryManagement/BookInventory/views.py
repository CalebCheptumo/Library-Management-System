from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import Author, Book

@login_required
def library(request):
    return render(request, 'library.html')
@login_required
def inventory(request):
    return render(request, 'inventory.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('library')  # Redirect to a success page
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def author_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:  # Check if name is not empty
            if Author.objects.filter(name=name).exists():
                messages.warning(request, 'Author with this name already exists')
            else:
                author = Author(name=name)
                author.save()
                messages.success(request, 'Author added successfully')
            return redirect('author_form')
        else:
            messages.warning(request, 'Please fill in all required fields')
    return render(request, 'author_form.html')

def book_form_view(request):
    authors = Author.objects.all()  # Define authors here
    form_data = {}

    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        publication_date = request.POST.get('publication_date')
        isbn = request.POST.get('isbn')
        available = request.POST.get('available') == 'on'

        form_data = {
            'title': title,
            'author_id': author_id,
            'publication_date': publication_date,
            'isbn': isbn,
            'available': available
        }

        if title and author_id and publication_date and isbn:
            author = Author.objects.get(id=author_id)
            book = Book(title=title, author=author, publication_date=publication_date, isbn=isbn, available=available)
            book.save()
            messages.success(request, 'Book added successfully')
            return redirect('book_form')
        else:
            messages.warning(request, 'Please fill in all required fields')
    return render(request, 'book_form.html', {'authors': authors})
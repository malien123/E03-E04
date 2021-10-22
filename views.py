from django.shortcuts import render, redirect
from .models import Book,Review
from .forms import BookForm, ReviewForm, EntryForm

def index(request):
    #home page 

    return render(request, 'book/index.html')


#shows all books
def books(request):
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'book/books.html', context)

#show all reviews
def reviews(request):
    reviews = Review.objects.order_by('date_added')
    context = {'reviews': reviews}
    return render(request, 'book/reviews.html', context)



#show a single book and all its entries
def book(request, book_id):
    book = Book.objects.get(id=book_id)
    entries = book.entry_set.order_by('-date_added')
    context = {'book' : book, 'entries' : entries}
    return render(request, 'book/book.html', context)

#show a single review and all its entries
def review(request, review_id):
    review = Review.objects.get(id=review_id)
    entries = review.entry_set.order_by('-date_added')
    context = {'review' : review, 'entries' : entries}
    return render(request, 'book/review.html', context)

#add a new book
def new_book(request):
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = BookForm()
    else:
        #POST submitted; process data
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:books')


    #display form
    context = {'form' : form}
    return render(request, 'book/new_book.html', context)

#add a new review
def new_review(request):
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = ReviewForm()
    else:
        #POST submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('book:reviews')


    #display form
    context = {'form' : form}
    return render(request, 'book/new_review.html', context)



def new_entry_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method != 'POST':
        #no data, create blank form
        form = EntryForm()
    else:
        #POST data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_book = form.save(commit=False)
            new_entry_book.book = book
            new_entry_book.save()
            return redirect('book:book', book_id=book_id)
    
    #display form

    context = {'book': book, 'form' : form}
    return render(request, 'book/new_entry_book.html', context)



def new_entry_review(request, review_id):
    review = Review.objects.get(id=review_id)

    if request.method != 'POST':
        #no data, create blank form
        form = EntryForm()
    else:
        #POST data submitted
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_review = form.save(commit=False)
            new_entry_review.review = book
            new_entry_review.save()
            return redirect('book:review', reivew_id=review_id)
    
    #display form

    context = {'review': review, 'form' : form}
    return render(request, 'book/new_entry_review.html', context)
            
            

    
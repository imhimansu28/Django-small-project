from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookForm
from .models import Book

# Create your views here.


# this is the curd operation
def create_book(request):
    book = Book.objects.all().order_by('-created_date')
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curd:book')
    else:
        form = BookForm()
    context = {'form': form, 'book': book}
    return render(request, 'create.html', context)


def view_book(request, id):
    book = Book.objects.get(id=id)
    context = {'book': book}
    return render(request, 'view.html', context)


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(instance=book, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('curd:book')
    else:
        form = BookForm(instance=book)

    return render(request, "edit.html", {"form": form, "book": book})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('curd:book')

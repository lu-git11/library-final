from django.shortcuts import render
from .forms import BookForm
from .models import Book
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
#def InventoryView(request):
#    books_list = Book.objects.all()
#   return render(request, 'inventory/inventory.html', {'books_list': books_list})

class InventoryListView(ListView):
    model = Book
    template_name = 'inventory/inventory.html'
    context_object_name = 'books_list'

class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/add_book.html'
    success_url = reverse_lazy('inventory')

class UpdateBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'inventory/edit.html'
    success_url = reverse_lazy('inventory')


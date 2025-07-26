from django.urls import path
from . import views

urlpatterns = [
    path('inventory/', views.InventoryListView.as_view(), name='inventory'),
    path('add_book/', views.AddBookView.as_view(), name='add_book'),
    path('edit_book/<int:pk>/', views.UpdateBookView.as_view(), name='edit_book'),
    #path('inventory/', views.InventoryView, name='inventory'),
]
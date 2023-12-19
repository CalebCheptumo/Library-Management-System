from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='book_inventory'), 
    path('author_form/', views.author_form_view, name= 'author_form'),
    path('book_form/', views.book_form_view, name= 'book_form'),
]
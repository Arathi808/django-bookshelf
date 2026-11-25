from django.urls import path
from.import views

urlpatterns=[
    path('',views.home,name='home'),
    path('books/', views.book_list, name='book_list'),
    path('add/',views.add_book,name='add_book'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),
    path('about/', views.about, name='about'),
]

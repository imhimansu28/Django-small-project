from django.urls import path

from . import views

app_name = 'curd'
urlpatterns = [
    path("", views.create_book, name="book"),
    path('view/<int:id>', views.view_book, name='view_book'),
    path('<int:id>', views.delete_book, name='delete'),
    path('edit/<int:id>', views.edit_book, name='edit_book'),
]

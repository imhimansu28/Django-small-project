from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField(blank=True)
    year_published = models.DateField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60, blank=True)
    publish = models.BooleanField(default=True)

    def __str__(self):
        return self.book_name

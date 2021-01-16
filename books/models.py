from django.db import models

# Create your models here.


class Book(models.Model):
    book_id = models.PositiveIntegerField(unique=True)
    genre = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    title_normalized = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(default='')

    def __str__(self):
        return self.title

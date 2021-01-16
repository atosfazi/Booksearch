from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_id", "genre", "title", 'title_normalized', "author", "description")


admin.site.register(Book, BookAdmin)

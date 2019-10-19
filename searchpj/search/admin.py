from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("book", "author", "urls")

admin.site.register(Book, BookAdmin)

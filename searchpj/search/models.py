from django.db import models


class Book(models.Model):
    book = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    urls = models.URLField(max_length=100)
    texts = models.TextField()

    class Meta:
      verbose_name_plural = "books"

    def __str__(self):
        return self.book

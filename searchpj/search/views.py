from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchsResultsView(ListView):
    model = Book
    template_name = 'searchs_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(book__icontains=query) | Q(author__icontains=query) |
            Q(texts__icontains=query)
        )
        return object_list

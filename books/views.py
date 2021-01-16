from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import Book
import numpy as np
from unidecode import unidecode
from django.conf import settings


class HomePageView(TemplateView):
    template_name = 'home.html'


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):
        '''https://docs.djangoproject.com/en/3.1/ref/models/querysets/#queryset-api'''
        query = self.request.GET.get('q')
        if len(query) <= 2:
            return None
        object_list = Book.objects.filter(
            Q(title_normalized__icontains=unidecode(query)) | Q(author__icontains=unidecode(query))
        )
        return object_list


class RecommenderResultsView(ListView):
    model = Book
    template_name = 'similar_books_results.html'
    # get loaded embedding weights end embedding indexes dict
    weights = getattr(settings, "EMBEDDINGS_WEIGHTS", None)
    id_idx_dict = getattr(settings, "TITLE_IDX_DICT", None)
    idx_id_dict = {v: k for k, v in id_idx_dict.items()}

    def get_queryset(self):
        query = self.request.GET.get('p')
        recommendations = self.find_recommendation(query)
        object_list = Book.objects.filter(Q(book_id__in=recommendations))
        return object_list

    def find_recommendation(self, book_id, n=4):
        # calculate distances between books
        book_idx = self.id_idx_dict[int(book_id)]
        dists = np.dot(self.weights, self.weights[book_idx])
        sorted_dists = np.argsort(dists)

        # Get elements closest to sample
        closest = list(sorted_dists[-n:])
        if book_idx in closest:
            closest.remove(book_idx)
        closest = [self.idx_id_dict[idx] for idx in closest]
        return closest

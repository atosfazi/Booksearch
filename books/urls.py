from django.urls import path

from .views import HomePageView, SearchResultsView, RecommenderResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('similar/', RecommenderResultsView.as_view(), name='similar_books_results'),
    path('', HomePageView.as_view(), name='home'),
]
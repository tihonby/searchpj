from django.urls import path

from .views import HomePageView, SearchsResultsView

urlpatterns = [
    path('searchs/', SearchsResultsView.as_view(), name='searchs_results'),
    path('', HomePageView.as_view(), name='home'),
]

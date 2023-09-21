from django.urls import path
from . import views



urlpatterns = [
    path('listproducts', views.ProductListView.as_view() ),
    path('search', views.SearchProductView.as_view()),
    
]
urlpatterns = [
    path('listproducts', views.ProductListView.as_view() ),
    path('search', views.SearchProductView.as_view()),
    
]
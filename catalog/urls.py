from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeListView, ProductDetailView, ProductCreateView, BlogCreateView, BlogUpdateView, \
    BlogListView, BlogDetailView, BlogDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_details'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blog_details/<int:pk>/', BlogDetailView.as_view(), name='blog_details'),
    path('blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]

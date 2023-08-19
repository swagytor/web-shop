from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_details

app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='homepage'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product_details, name='product_details'),
]

from django.urls import path
from . import views

urlpatterns = [
	path("product/", views.ProductListCreate.as_view(), name="product"),
	path("remove-products/", views.ProductDelete.as_view(), name="delete-product"),
]
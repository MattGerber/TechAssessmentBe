from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CustomerViewSet, ProductDeleteViewSet, ProductListCreate, OrderListCreate, ProductsListCreate

router = SimpleRouter()
router.register(r"remove-products", ProductDeleteViewSet, "api")
router.register(r"product", ProductListCreate, "product")
router.register(r"products", ProductsListCreate, "products")
router.register(r"customer", CustomerViewSet, "customer")

urlpatterns = [
	# path("product/", ProductListCreate.as_view(), name="product"),
	path("order/", OrderListCreate.as_view(), name="orders"),
	# path("remove-products/", views.ProductDelete.as_view(), name="delete-product"),
	path("", include(router.urls))
]
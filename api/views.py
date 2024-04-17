from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Order

# Create your views here.
class ProductListCreate(generics.ListCreateAPIView):
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Product.objects.all()
	
class OrderListCreate(generics.ListCreateAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	# Order.objects.filter(customerId= User, paid=False)
	def get_queryset(self):
		user = self.request.user
		return Order.objects.all()
	
	def perform_create(self, serializer):
		if serializer.is_valid():
			serializer.save(self.request.user)
		else:
			print(serializer.error)

class ProductDelete(generics.DestroyAPIView):
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]

		# products = self.request.data
		# return Product.objects.filter(id= products)
	def get_queryset(self):
		return Product.objects.all()
	
class CreateUserView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [AllowAny]

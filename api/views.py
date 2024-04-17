from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Order

# Create your views here.
class ProductListCreate(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Product.objects.all()

class CustomerViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	
class OrderListCreate(generics.ListCreateAPIView):
	serializer_class = OrderSerializer
	permission_classes = [IsAuthenticated]

	# Order.objects.filter(customerId= User, paid=False)
	def get_queryset(self):
		user = self.request.user
		return Order.objects.all()
	
	def perform_create(self, serializer):
		if serializer.is_valid():
			serializer.save(customerId=self.request.user)
		else:
			print(serializer.error)

class ProductDeleteViewSet(viewsets.ModelViewSet):
	serializer_class = ProductSerializer
	permission_classes = [IsAuthenticated]
	queryset = Product.objects.all()

	def delete(self, request):
		records = self.queryset.filter(id__in=self.request.data)
		records.delete()
		return  Response(status=status.HTTP_204_NO_CONTENT)
		# products = self.request.data
		# return Product.objects.filter(id= products)
	
class CreateUserView(generics.CreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = [AllowAny]

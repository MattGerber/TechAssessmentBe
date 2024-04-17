from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Order

class UserSerializer(serializers.ModelSerializer):
	name = serializers.CharField(source='username')
	class Meta:
		model = User
		fields = ["id", "name", "password", "email"]
		extra_kwargs = {"password": {"write_only": True}}

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user
	
class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ["id", "name", "description", "price"]

class OrderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Order
		fields = ["id", "paid", "customerId", "products", "total"]
		extra_kwargs = {"customerId": {"read_only": True}}
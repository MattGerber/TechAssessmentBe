from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	price = models.DecimalField(max_digits=19, decimal_places=2)

	def __str__ (self):
		return self

class Order(models.Model):
	paid = models.BooleanField()
	customerId = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
	products = models.JSONField()
	total = models.DecimalField(max_digits=19, decimal_places=2)

	def __str__ (self):
		return self

from django.db import models

class order(models.Model):
	slug = models.CharField(max_length=50)
	address = models.CharField(max_length=50, null=True)
	orderType = models.CharField(max_length=50,null=True)
	ownedBy = models.CharField(max_length=50,null=True)
	status = models.CharField(max_length=50,null=True)
	estimatedDeliveryDate = models.DateTimeField(max_length=50)
	shippingCost = models.DecimalField(max_digits=10,decimal_places=2)
	specialDiscout = models.DecimalField(max_digits=5,decimal_places=2)
	tax = models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return self.slug

	class Meta:
		ordering = ('id',)

class product(models.Model):
	"""docstring for product"""
	sku = models.CharField(max_length=50)
	description = models.CharField(max_length=300)
	brand = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=10,decimal_places=2)
	discount = models.DecimalField(max_digits=5,decimal_places=2)
	stock = models.CommaSeparatedIntegerField(max_length=10)

	def getNetPrice(self):
		return self.price-(self.price*self.discount/100)

	def __str__(self):
		return self.sku

	class Meta:
		ordering = ('sku',)

class productListedInOrder(models.Model):
	order = models.ForeignKey(order,on_delete=models.CASCADE)
	product = models.ForeignKey(product,on_delete=models.CASCADE)
	class Meta:
		ordering = ('order',)



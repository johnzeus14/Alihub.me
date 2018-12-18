from django.db import models

from django.conf import settings

from rest_framework.reverse import reverse



class ProductManager(models.Manager):

	
	def filter_by_instance(self, instance):
		user 			= 	instance.user
		qs				= super(ProductManager, self).filter(user = user)
		return qs

class Product(models.Model):
	user 		 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	product_name 		 	= models.CharField(max_length = 300, verbose_name ='product name' )
	product_description  	= models.CharField(max_length = 3000)
	product_image 			= models.FileField()
	product_price 			= models.DecimalField(max_digits = 9, decimal_places  = 2)

	created_at 				= models.DateTimeField(auto_now_add= True)
	objects 				= ProductManager()


	def __str__(self):
		return self.product_name

	def get_api_url(self):
		return reverse('product:product-detail', kwargs = {'id':self.id})

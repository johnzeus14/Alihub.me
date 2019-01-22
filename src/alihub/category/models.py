from django.db import models

from django.conf import settings
from rest_framework.reverse import reverse




class Category(models.Model):
	user 		=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


	title 		= 	models.CharField(max_length = 3000)
	media 		= 	models.FileField(blank = True)


	def __str__(self):
		return self.title



	def get_api_url(self):
		return reverse('category:category-detail', kwargs = {'title':self.title})


from django.db import models

from django.conf import settings





class Category(models.Model):
	user 		=	models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)


	title 		= 	models.CharField(max_length = 3000)
	media 		= 	models.FileField(blank = True)


	def __str__(self):
		return self.title



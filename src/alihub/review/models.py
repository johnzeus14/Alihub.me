from django.db import models
from django.conf import settings
from rest_framework.reverse import reverse


class ReviewManager(models.Manager):


	def filter_by_instance(self, instance):
		user 			= 	instance.user
		qs				= super(ReviewManager, self).filter(user = user)
		return qs





class Review(models.Model):
	user		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'author')
	target 		= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	content 	= models.CharField(max_length = 300)
	media 		= models.FileField(blank = True)
	

	created_at  = models.DateTimeField(auto_now_add = True)

	objects 	= ReviewManager()

	def __str__(self):
		return str(self.target) + 'Review'


	def get_api_url(self):
		return reverse('review:review-detail', kwargs = {'id':self.id})


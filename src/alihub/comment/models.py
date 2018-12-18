from django.db import models


from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CommentManager(models.Manager):
	
	def filter_by_instance(self, instance):
		target 			= ContentType.objects.get_for_model(instance.__class__)
		obj_id 			=  instance.id
		qs				= super(CommentManager, self).filter(target = target, object_id=obj_id)
		return qs

class Comment(models.Model):
	user   		 				=  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	target 						= models.ForeignKey(ContentType, on_delete =  models.CASCADE)
	object_id 					= models.PositiveIntegerField()
	Content_object				= GenericForeignKey('target', 'object_id')
	

	content 	 				= models.CharField(max_length = 1000)
	media    	 				= models.FileField(blank = True)
	created_at 	 				=  models.DateTimeField(auto_now_add = True) 


	objects 					= CommentManager()






	def __str__(self):
		return str(self.user.full_name) + '-'+' Comment'

	@property
	def owner(self):
		return self.user

	


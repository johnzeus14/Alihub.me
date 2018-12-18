from django.db import models

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class LikeManager(models.Manager):
	
	def filter_by_instance(self, instance):
		content_type 	= ContentType.objects.get_for_model(instance.__class__)
		obj_id 			=  instance.id
		qs				= super(LikeManager, self).filter(content_type = content_type, object_id=obj_id)
		return qs


class Like (models.Model):
	user    					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

	target 						= models.ForeignKey(ContentType, on_delete =  models.CASCADE)
	object_id 					= models.PositiveIntegerField()
	Content_object				= GenericForeignKey('target', 'object_id')

	liked      					=  models.BooleanField(default = False)

	created_at   				= models.DateTimeField(auto_now_add = True)

	objects  					= LikeManager()


	def __str__(self):
		return str(self.user.full_name)

		
	@property
	def owner(self):
		return self.user

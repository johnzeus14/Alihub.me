from django.db import models

from django.conf import settings 


from rest_framework.reverse import reverse
from django.contrib.contenttypes.models import ContentType



		
class PostManager(models.Manager):

	def filter_by_instance(self, instance):
		user 			= instance.user	
		qs				= super(PostManager, self).filter(user = user)
		return qs






class Post(models.Model):
	user       		 =    models.ForeignKey(settings.AUTH_USER_MODEL , on_delete = models.CASCADE)

	content    		 = 	models.CharField(max_length = 1000)
	
	media       	 =  models.FileField(blank = True)


	created_at  	 = models.DateTimeField(auto_now_add = True)

	objects 		 =  PostManager()




	def __str__(self):
		return str(self.user.full_name)+'-'+ 'post'

	def get_api_url(self):
		return reverse('post:post-detail', kwargs = {'id':self.id})


	@property
	def owner(self):
		return self.user

		
	@property
	def extra_activity_data(self):
		return {
				'content': self.content ,
				'image':self.image,
				'video':self.video,
		}

	@property
	def get_content_type(self):
		instance 		= self
		content_type    = ContentType.objects.get_for_model(instance.__class__)
		return content_type
	
	
	
	
		
	



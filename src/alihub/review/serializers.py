from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Review






class ReviewSerializer(ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	class Meta:
		model 	=	Review
		fields	=	[
			'id',
			'user',
			'avatar',
			'content',
			'target',
			'media',
			'created_at',
			
		]


		

	def get_user(self, obj):
		return str(obj.user.profile.username)


	def get_avatar(self,obj):
		try:
			avatar = str(obj.user.profile.avatar)
		except:
			avatar = None
		return avatar


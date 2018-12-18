from rest_framework.serializers import (
	
	ModelSerializer,
	SerializerMethodField,

		)


from .models import Like









class LikeSerializer(ModelSerializer):
	class Meta:
		model 	=	Like
		fields	=	[
			'id',
			'user',
			'target', 			
			'object_id' ,	
			'likes_count',
			'liked',
			'created_at',
		
			
		]

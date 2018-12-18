from rest_framework.serializers import (
	ModelSerializer,
	SerializerMethodField,

	)
 
from .models import Product






class ProductSerializer(ModelSerializer):
	

	user  =  SerializerMethodField()
	avatar = SerializerMethodField()
	class Meta:
		model 	=	Product
		fields	=	[
			'id',
			'user',
			'avatar',
			'product_name',
			'product_description',
			'product_image',
			'product_price',
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


from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (

	ModelSerializer,
	SerializerMethodField,
	
	
	)
from comment.models import Comment
from comment.serializers import CommentSerializer
from .models import Post


from like.models import Like
from like.serializers import LikeSerializer




class PostSerializer( ModelSerializer):	
	avatar  	=  	SerializerMethodField()
	user 		=  SerializerMethodField()
	
	
	class Meta:
		model 	=	Post
		fields	=	(
			'id',
			'user',
			'avatar',
			'content',
			'media',
			# 'comments',
		

			
		)

		read_only_fields = ['user']
	# def get_comments(self, obj):
	
	# 	content_type = obj.get_content_type
	# 	object_id   = obj.id
	# 	c_qs 		=  Comment.objects.filter_by_instance(obj).count()
	# 	comments    = CommentSerializer(c_qs, many = True).data
	# 	return comments


		

	def get_user(self,obj):
		return str(obj.user.profile.username)


	def get_avatar(self,obj):
		try:
			avatar  = str(obj.user.profile.avatar)
		except:
			avatar  = None
		return avatar

	





class PostDetailSerializer( ModelSerializer):
	avatar  		=  	SerializerMethodField()
	comments    	=  SerializerMethodField()

	class Meta:
		model 	=	Post
		fields	=	(
			'id',
			'user',
			'avatar',
			'content',
			'media',
			'created_at',
			'comments',	
			
		)
		read_only_fields = ['user']


	



		

	def get_user(self, obj):
		return str(obj.user.profile.username)

	def get_avatar(self, obj):
		try:
			avatar  = str(obj.user.profile.avatar)
		except:
			avatar  = None
		return avatar

	def get_comments(self, obj):
	
		content_type = obj.get_content_type
		object_id   = obj.id
		c_qs 		=  Comment.objects.filter_by_instance(obj)
		comments    = CommentSerializer(c_qs, many = True).data
		return comments

	# def get_likes(self, obj):
	# 	content_type   =  obj.get_content_type
	# 	object_id  		=  obj.id
	# 	l_qs 			= Like.objects.filter_by_instance(obj)
	# 	likes 			= LikeSerializer(l_qs, many = True).data
	# 	return likes




		




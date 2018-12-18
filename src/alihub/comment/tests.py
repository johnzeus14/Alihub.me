# from  rest_framework.test import APITestCase
# from rest_framework.reverse import reverse
# from rest_framework import status


# from rest_framework_jwt.settings import api_settings

# payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# encode_handler  = api_settings.JWT_ENCODE_HANDLER



# from django.contrib.auth import get_user_model


# from .models import Comment
# from django.contrib.contenttypes.models import ContentType


# from story.models import Story


# User = get_user_model()

# content_type  = ContentType.objects.get_for_model(Story)

# class StoryAPITestCase(APITestCase):


# 	def setUp(self):

# 		user_obj  = User( email = 'zeus@gmail.com', full_name = 'john benjamin')
# 		user_obj.set_password ('oldskool123')
# 		user_obj.save()

# 		story = Story.objects.create(
# 			user         	=   user_obj,
# 			content  		= 'hello world',
# 			image    		= None,
# 			)

	

# 		comment = Comment.objects.create(
# 			user         		  =   user_obj,
# 			content_type          = content_type,
# 			object_id   	   	  = 1,
# 			content  		 	  = 'hello world',
# 			image    			  = None,
# 			)



# 	def test_single_user(self):
# 		user_obj = User.objects.count()
# 		self.assertEqual(user_obj, 1)


# 	def test_single_comment(self):
# 		comment  = Comment.objects.count()
# 		self.assertEqual(comment, 1)


# 	def test_get_list(self):
		
# 		data			 = {}
# 		url 			 = reverse('comment:comment-list')
# 		response 		 = self.client.get(url, data, format = 'json')
# 		self.assertEqual = (response.status_code, status.HTTP_200_OK)


# 	def test_post_comment(self):
	
		
# 		data			 = {

# 			'content_type'  :	8,
# 			'object_id'   	: 1,
# 			'content'  		:'My first comment',
# 			'image'    		:None,
# 			}
# 		url 			 = reverse('comment:comment-list')
# 		print(data)
# 		response 		 = self.client.post(url, data, format = 'json')
# 		self.assertEqual = (response.status_code, status.HTTP_200_OK)


# 	# def test_put_comment(self):
		
# 	# 	data			 = {

# 	# 		'content_type'  :'content_type',
# 	# 		'object_id'   	: 1,
# 	# 		'content'  		:'My first comment',
# 	# 		'image'    		:None,
# 	# 		}
# 	# 	url 			 = reverse('comment:comment-list')
# 	# 	response 		 = self.client.post(url, data, format = 'json')
# 	# 	self.assertEqual = (response.status_code, status.HTTP_200_OK)


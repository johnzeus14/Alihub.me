# from  rest_framework.test import APITestCase
# from rest_framework.reverse import reverse
# from rest_framework import status


# from rest_framework_jwt.settings import api_settings

# payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# encode_handler  = api_settings.JWT_ENCODE_HANDLER



# from django.contrib.auth import get_user_model

# from .models import Like
# from story.models import Story
# from userprofile .models import Profile

# User = get_user_model()



# class LikeAPITestCase(APITestCase):


# 	def setUp(self):

# 		user_obj  = User( email = 'zeus@gmail.com', full_name = 'john benjamin')
# 		user_obj.set_password ('oldskool123')
# 		user_obj.save()

# 		profile = Profile.objects.create(
# 			user  			= user_obj,
# 			username		= 'zeus',
# 			avatar			= None,
# 			bio				= 'The official page of Alihub',
# 			category 		= 'Telecomunication',
# 			country 		=  'USA',

# 			)

# 		story = Story.objects.create(
# 			user         	=   user_obj,
# 			content  		= 'hello world',
# 			image    		= None,
# 			video 			= None,
# 			)
# 		like  = Like.objects.create(
# 			user 		= user_obj,
# 			target		 = 'story',
# 			object_id	  = 1,
# 			likes_count 	 = 1,
# 			liked			=	True,
# 			)



# 	def test_single_user(self):
# 		user_obj = User.objects.count()
# 		self.assertEqual(user_obj, 1)


# 	def test_single_story(self):
# 		story  = Story.objects.count()
# 		self.assertEqual(story, 1)

# 	def test_single_like(self):
# 		like  	= Like.objects.count()
# 		self.assertEqual(like, 1)



# 	
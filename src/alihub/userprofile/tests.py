# from  rest_framework.test import APITestCase
# from rest_framework.reverse import reverse
# from rest_framework import status


# from rest_framework_jwt.settings import api_settings

# payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# encode_handler  = api_settings.JWT_ENCODE_HANDLER



# from django.contrib.auth import get_user_model
# from django.contrib.auth import authenticate


# from .models import Profile


# User = get_user_model()



# class ProfileAPITestCase(APITestCase):


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
# 			country 		=  'Nigeria',
# 			phone 			=  '0809740825',
# 			website 		= 'alihub.com',
			

# 			)



# 	def test_single_user(self):
# 		user_obj = User.objects.count()
# 		self.assertEqual(user_obj, 1)
# 		print(user_obj)


# 	def test_single_profile(self):
# 		profile  = Profile.objects.count()
# 		self.assertEqual(profile, 1)

# 	def test_create_profile(self):
# 		user_obj    =  User.objects.first()
# 		payload 	= payload_handler(user_obj)
# 		token_rsp	= encode_handler(payload)
# 		self.client.credentials(HTTP_AUTHORIZATION = 'JWT'+ token_rsp)
		
# 		data       = {
			
# 			'username' 	:'zeus',
# 			'avatar'   	:None,
# 			'bio'	   	:'my first status',
# 			'category'	:'Religion',
# 			'country'	:'NIG',

# 		}
# 		url  		= reverse('profile:profile-create')
# 		response	 = self.client.post(url, data, format = 'json')
# 		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED )

# 	def test_update_profile(self):
# 		obj 			= Profile.objects.first()
		
		
# 		user_obj		= User.objects.first()
# 		payload 		= payload_handler(user_obj)
# 		token_rsp		= encode_handler(payload)

# 		self.client.credentials(HTTP_AUTHORIZATION = 'JWT'+ token_rsp)
# 		url 			= obj.get_api_url()
# 		data			= {

# 				'username'	:	'alihub',
# 				'avatar'	:	None,
# 				'bio'		:	'hello world',
# 				'category'	: 	'Religion',
# 				'country'	:	'NIG',

# 		}
	
		
	
# 		response 		 = self.client.put(url, data, format = 'json')
# 		print(response.data)
# 		self.assertEqual(response.status_code, status.HTTP_200_OK)

	

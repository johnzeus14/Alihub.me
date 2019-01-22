from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


from rest_framework_jwt.settings import api_settings
payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler  = api_settings.JWT_ENCODE_HANDLER



from django.contrib.auth import get_user_model
from .models import Category
from userprofile.models import Profile

User = get_user_model()



class CategoryAPITestCase(APITestCase):


	def setUp(self):

		user_obj  = User( email = 'zeus@gmail.com', full_name = 'john benjamin')
		user_obj.set_password ('oldskool123')
		user_obj.save()

		profile = Profile.objects.create(
			user  			= user_obj,
			username		= 'zeus',
			avatar			= None,
			bio				= 'The official page of Alihub',
			category 		= 'Telecomunication',
			country 		=  'Nigeria',
			phone 			=  '0809740825',
			website 		= 'alihub.com',


			)

		category = Category.objects.create(
			user         	=   user_obj,
			title  			= 'Internet company',
			media    		= None,
		
			)



	def test_single_user(self):
		user_obj = User.objects.count()
		self.assertEqual(user_obj, 1)
		print(user_obj)


	def test_single_category(self):
		category  = Category.objects.count()
		self.assertEqual(category, 1)

	def test_get_category(self):
		
		data			 = {}
		url 			 = reverse('category:category-list')
		response 		 = self.client.get(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_200_OK)

	def test_post_category(self):
		user_obj  = User.objects.first()
		payload   = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		print(token_rsp)
		print(user_obj)

		self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
		data  			 = {
			'title': 'Banking and Finance',
			'media'  : None,
			

				}
		url 			 = reverse('category:category-list')
		response   	     = self.client.post(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_201_CREATED)

	# def test_put_category(self):
	# 	user_obj  = User.objects.first()
	# 	payload   = payload_handler(user_obj)
	# 	token_rsp = encode_handler(payload)
	# 	print(token_rsp)

	# 	self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
	# 	data  			 = {
	# 		'title': 'Agriculural company',
	# 		'media'  : None,
		

	# 			}
	# 	category      		 = Category.objects.first()
	# 	url 				 = category.get_api_url()
	# 	response    		 = self.client.put(url,data, format = 'json')
	# 	self.assertEqual	 = (response.status_code,status.HTTP_200_OK)


	# def test_delete_category(self):
	# 	data 		    = {}
	# 	category 		= Category.objects.first()
	# 	url 		    = category.get_api_url()
	# 	response 	    = self.client.delete(url, data, format = 'json')
	# 	self.assertEqual = (response.status_code, status.HTTP_200_OK)


	# def test_get_item_with_user(self):
	# 	user_obj  = User.objects.first()
	# 	payload   = payload_handler(user_obj)
	# 	token_rsp = encode_handler(payload)
	# 	self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)


	# 	post 		 = Post.objects.first()
	# 	url   		 = post.get_api_url()
	# 	data 		 = {}
	# 	response	 = self.client.get(url, data, format = 'json')
	# 	self.assertEqual(response.status_code, status.HTTP_200_OK )
		



	# def test_post_item_with_user(self):
	# 	user_obj  = User.objects.first()
	# 	payload   = payload_handler(user_obj)
	# 	token_rsp = encode_handler(payload)
	# 	self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
	# 	print(token_rsp)
	
	
	# 	url       = reverse('post:post-list')
	# 	data 	  =  {
	# 		'content': 'hello mars',
	# 		'media':	None,
	# 	}
	# 	response  = self.client.post(url, data, format ='json')
	# 	self.assertEqual(response.status_code, status.HTTP_400_UNAUTHORIZED)

	# def test_delete_item_with_user(self):
	# 	user_obj  = User.objects.first()
	# 	payload   = payload_handler(user_obj)
	# 	token_rsp = encode_handler(payload)
	# 	self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)


	# 	post 		 = Post.objects.first()
	# 	url   		 = post.get_api_url()
	# 	data 		 = {}
	# 	response	 = self.client.delete(url, data, format = 'json')
	# 	self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED )
		

		
		
	# # 	response    = self.client.post(url, data, format = 'json')
	# # 	self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
	# # 	print(payload)
	# # 	print(token_rsp)
		

	

		



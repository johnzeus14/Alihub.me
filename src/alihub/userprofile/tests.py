from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler  = api_settings.JWT_ENCODE_HANDLER



from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType




from .models import Profile



User = get_user_model()


class ProfileAPITestCase(APITestCase):


	def setUp(self):

		user_obj  = User( email = 'zeus@gmail.com', full_name = 'john benjamin')
		user_obj.set_password ('oldskool123')
		user_obj.save()

	
		profile = Profile.objects.create(
				user  			= user_obj,
				username		= 'ALihub',
				avatar			= None,
				bio				= 'The official page of Alihub',
				category 		= 'Telecomunication',
				country 		=  'Nigeria',
				phone 			=  '0809740825',
				website 		= 'alihub.com',

			)

	



	def test_single_user(self):
		user_obj = User.objects.count()
		self.assertEqual(user_obj, 1)


	def test_single_profile(self):
		profile  = Profile.objects.count()
		self.assertEqual(profile, 1)




	def test_post_profile_with_user(self):
		user_obj  = User.objects.first()
		payload   = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		print(token_rsp)
		print(user_obj)

		self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)

	
		
		data			 = {

				'username'		:'ALihub',
				'avatar'		: None,
				'bio'			: 'The official page of Alihub',
				'category' 		:'Telecomunication',
				'country' 		:  'Nigeria',
				'phone' 		: '0809740825',
				'website' 		: 'alihub.com',
		}
		url 			 = reverse('profile:profile-create')
		print(data)
		response 		 = self.client.post(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_200_OK)


	def test_put_review_with_user(self):
		user_obj  = User.objects.first()
		payload   = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		print(token_rsp)
		print(user_obj)

		self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
		
		
		data			 = {

				'username'		:'zenithbank',
				'avatar'		: None,
				'bio'			: 'The official page of Alihub',
				'category' 		:'Telecomunication',
				'country' 		:  'Nigeria',
				'phone' 		: '0809740825',
				'website' 		: 'alihub.com',
		}
		print(data)
		url 			 = reverse('profile:profile-detail')
		print(url)
		response 		 = self.client.post(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_200_OK)


	# def test_delete_review_with_user(self):
	# 	user_obj  = User.objects.first()
	# 	payload   = payload_handler(user_obj)
	# 	token_rsp = encode_handler(payload)
		
		

	# 	self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
		
	# 	data			 = {}
	# 	print( str(data) + 'the deleted data')
	# 	review 			= Review.objects.first()
	# 	url 			= review.get_api_url()

	
	# 	response 		 = self.client.delete(url, data, format = 'json')
	# 	self.assertEqual = (response.status_code, status.HTTP_200_OK)



	# # 	
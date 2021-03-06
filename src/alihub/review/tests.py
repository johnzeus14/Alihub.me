from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status


from rest_framework_jwt.settings import api_settings

payload_handler = api_settings.JWT_PAYLOAD_HANDLER
encode_handler  = api_settings.JWT_ENCODE_HANDLER



from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType




from .models import Review
from userprofile.models import Profile


User = get_user_model()


class ReviewAPITestCase(APITestCase):


	def setUp(self):

		user_obj  = User( email = 'zeus@gmail.com', full_name = 'john benjamin')
		user_obj.set_password ('oldskool123')
		user_obj.save()

		user_target  =  User( email = 'basketmouth@gmail.com', full_name = 'Basket benjamin')
		user_target.set_password ('oldskool123')
		user_target.save()

		review = Review.objects.create(
			user         	=   user_obj,
			target 			= 	user_target,
			content  		= 'my first Review',
			media    		= None,
			)

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
		self.assertEqual(user_obj, 2)


	def test_single_review(self):
		review  = Review.objects.count()
		self.assertEqual(review, 1)




	def test_post_review_with_user(self):
		user_obj  = User.objects.first()
		payload   = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		print(token_rsp)
		print(user_obj)

		self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)

	
		
		data			 = {

			'content'  		:'My first comment',
			'media'    		:None,
			}
		url 			 = reverse('review:review-list')
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

		
			'content'  		:'My last review',
			'image'    		:None,
			}
		print(data)
		url 			 = reverse('review:review-list')
		print(url)
		response 		 = self.client.post(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_200_OK)


	def test_delete_review_with_user(self):
		user_obj  = User.objects.first()
		payload   = payload_handler(user_obj)
		token_rsp = encode_handler(payload)
		
		

		self.client.credentials(HTTP_AUTHORIZATION = 'JWT' + token_rsp)
		
		data			 = {}
		print( str(data) + 'the deleted data')
		review 			= Review.objects.first()
		url 			= review.get_api_url()

	
		response 		 = self.client.delete(url, data, format = 'json')
		self.assertEqual = (response.status_code, status.HTTP_200_OK)



	# 	
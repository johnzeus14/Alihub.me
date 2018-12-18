from django.db import models


from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.reverse import reverse

# from django_countries.fields import CountryField

from story.models import Story
from product.models import Product
from review.models import Review


# CATEGORY = (
# 	('AVI', 'Aviation'),
# 	('HAB', 'Health and Beauty'),
# 	('ENT', 'Entertainemnt'),
# 	('FAS', 'Fashion'),
# 	('TEC', 'Technology'),
# 	('CON', 'Construction'),
# 	('FAN' ,'Food and Nutrition '),
# 	('EAC', 'Education and Consultancy'),
# 	('AUT', 'Automobile'),
# 	('OIG', 'Oil and Gas'),
# 	('BAC', 'Building and  Construction'),
# 	('HOT', 'Hotel'),
# 	('TEC', 'Telecomunication'),
# 	('MAN', 'Manufacturing'),
# 	('TRN', 'Transportation'),
# 	('EHC', 'Embassy and High Commission'),
# 	('AGC', 'Agriculture'),
# 	('ICM', 'Internet company'),
# 	('CAF', 'clearing and Fowarding'),
# 	('LOG', 'Logistics'),
# 	('ECC', 'E-commerce'),
# 	('SEM', 'Security / Military'),
# 	('GAP', 'Government and Parastatals'),
# 	('IAE', 'import and Export'),
# 	('REL', 'Religion'),
# 	('BAN', 'Banking'),

# 	)


class Profile (models.Model):
	

	user   		 		 = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'profile', on_delete = models.CASCADE)
	

	username     		 = models.CharField(unique = True, max_length = 300)
	avatar       		 = models.FileField( blank = True , default = "{% static avatar.jpg%}" )
	bio   		  		 = models.CharField(max_length = 400, blank = True, verbose_name ='About')
	website				 = models.CharField(max_length = 5000, blank =True)
	phone 				 = models.IntegerField()
	
	category     		 = models.CharField(max_length = 1000)


	country       		 = models.CharField(max_length = 1000)



	def __str__(self):
		return str(self.user.full_name)  + '- '+'profile'

	def get_api_url(self):
		return reverse('profile:profile-detail', kwargs = {'username':self.username})


	@property
	def owner(self):
		return self.user

	@property
	def story(self):
		instance = self
		return Story.objects.filter_by_instance(instance)

	@property
	def product(self):
		instance = self
		return Product.objects.filter_by_instance(instance)

	@property
	def review(self):
		instance = self
		return Review.objects.filter_by_instance(instance)
	


	# def create_profile(sender,**kwargs ):
	# 	if kwargs['created']:
	# 		user_profile=Profile.objects.create(user=kwargs['instance'])

	# post_save.connect(create_profile, sender=settings.AUTH_USER_MODEL)	

	




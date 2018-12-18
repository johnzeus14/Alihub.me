from rest_framework.serializers import (

	ModelSerializer,
	SerializerMethodField,
	ChoiceField,

	) 

from .models import Profile


from django_countries.serializers import CountryFieldMixin
# from accounts.serializers import AccountDetailSerializer
# from accounts.serializers import AccountDetailSerializer
from django.contrib.auth import get_user_model

from story.serializers import StorySerializer
from story.models import Story

from product.serializers import ProductSerializer
from product.models import Product

from review.serializers import ReviewSerializer
from review.models import Review



User  = get_user_model()





class ProfileCreateSerializer(CountryFieldMixin, ModelSerializer):


	class Meta:
		model = Profile

		fields = [
			'id',
			'user',
			'username',
			'avatar',
			'country',
			'category',
			'website',
			'phone',
			'bio',

		
		]
	
	def validate_username(self, value):
		qs  = Profile.objects.filter(username__iexact = value)
		if qs.exists():
			raise serializers.ValidationError('Username already exist please pick another one')
		return value


 

class ProfileDetailSerializer( CountryFieldMixin, ModelSerializer):

	story 		 = SerializerMethodField()
	review 		 = SerializerMethodField()
	product 	 = SerializerMethodField()

	
	class Meta:
		model 	=	Profile
		fields	=	(
			'user',
			'id',
			'username',
			'avatar',
			'bio',
			'category',
			'country',
			'story',
			 'product',
			 'review',	
		
		)
		read_only_fields = ['story', 'product', 'review']

	


	def validate_username(self, value):
		qs 	= Profile.objects.filter(username__iexact = value)
		if self.instance:
			qs = qs.exclude(id =self.instance.id)
		if qs.exists():
			raise serializers.ValidationError('Username already exist please pick another one')
		return value


	def get_story(self, obj ):
		story  		= obj.story
		c_qs 		 =  Story.objects.filter_by_instance(obj)
		story   	 = StorySerializer(c_qs, many = True).data
		return story

	def get_product(self, obj):
		product 	= obj.product
		p_qs 		= Product.objects.filter_by_instance(obj)
		product 	= ProductSerializer(p_qs,many = True).data
		return product

	def get_review(self, obj):
		review 		= obj.review
		r_qs 		= Review.objects.filter_by_instance(obj)
		review 	 	= ReviewSerializer(r_qs,many = True).data
		return review

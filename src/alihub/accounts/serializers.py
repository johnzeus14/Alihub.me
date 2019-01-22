from rest_framework import serializers

from django.contrib.auth import get_user_model

User  = get_user_model()







class Registration(serializers.ModelSerializer):
	class Meta:
		model     = User
		fields  = [
			'full_name',
			'email',
			'password',
			'token',
		]
		extra_kwargs = {'password':
			{'write_only':True}

			}


	def create(self, validated_data):

		user = User(
		email=validated_data['email'],
		full_name=validated_data['full_name'],
		token = validated_data['token']

		)

		user.set_password(validated_data['password'])
		user.save()

		return user

	def validate_email(self, value):
		qs  = User.objects.filter(email__iexact = value)
		if qs.exists():
			raise serializers.ValidationError('Email already exist please pick another one')
		return value

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)


	




class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model 	=	User
		fields	=	[
			'id',
			'full_name',
			'email',
			'account_type',
			'verified',
		
			
		]


		read_only_fields = ['pk','verified']


	def validate_email(self, value):
		qs  = User.objects.filter(email__iexact = value)
		if self.instance:
			qs = qs.exclude(pk =self.instance.pk)
		if qs.exists():
			raise serializers.ValidationError('Email already exist please pick another one')
		return value
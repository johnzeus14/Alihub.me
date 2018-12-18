
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

class FacebookLogin(SocialLoginView):
	adapter_class = FacebookOAuth2Adapter


	


# from rest_framework import generics

# from rest_framework.permissions import (

# 	AllowAny,
# 	)


# from .serializers import (
# 	AccountCreateSerializer,
# 	AccountDetailSerializer,
# 	)


# from .permissions import IsOwnerOrReadOnly


# from django.contrib.auth import get_user_model

# User  = get_user_model()




# class RegisterAPIView(generics.CreateAPIView):
# 	serializer_class   = AccountCreateSerializer
# 	permission_classes = (AllowAny,)


# 	def get_queryset(self):
# 		User.objects.all()







# class AccountRudView(generics.RetrieveUpdateDestroyAPIView):
# 	lookup_field		=	'id'
# 	serializer_class	=	AccountDetailSerializer
# 	permission_classes  =  (IsOwnerOrReadOnly,)



# 	def get_queryset(self):
# 		return User.objects.all()



# 	def perform_update(self, serializer):
# 		serializer.save(user = self.request.user)
		


# 	def perform_delete(self, serializer):
# 		serializer.save(user = self.request.user)
from rest_framework import generics
from rest_framework.permissions import (

		IsAuthenticated,

				)

from .serializers import(

	ProfileCreateSerializer,
	ProfileDetailSerializer,

	) 
from .models import Profile
from .permissions import IsOwnerOrReadOnly









class ProfileAPIView(generics.CreateAPIView):
	lookup_field 	 = 'username'
	serializer_class  = ProfileCreateSerializer
	permissions_classes = (IsAuthenticated,)

	def get_queryset(self):
		return Profile.objects.all()









class ProfileRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		 	=	'username'
	serializer_class	 	=	ProfileDetailSerializer
	permissions_classes  	= (IsOwnerOrReadOnly)


	def get_queryset(self):
		return Profile.objects.all()


	

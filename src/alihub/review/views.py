
from rest_framework import generics




from .serializers import ReviewSerializer
from .models import Review

from .permissions import IsOwnerOrReadOnly


class ReviewAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = ReviewSerializer
	

	def get_queryset(self):
		return Review.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class ReviewRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	ReviewSerializer


	def get_queryset(self):
		return Review.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	
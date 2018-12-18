
from rest_framework import generics




from .serializers import ProductSerializer
from .models import Product

from .permissions import IsOwnerOrReadOnly


class ProductAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = ProductSerializer
	

	def get_queryset(self):
		return Product.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class ProductRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	ProductSerializer


	def get_queryset(self):
		return Product.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	
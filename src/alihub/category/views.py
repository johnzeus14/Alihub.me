
from rest_framework import generics

from .serializers import CategorySerializer
from .models import Category





class CategoryAPIView(generics.ListAPIView):
	lookup_field      =  'title'
	serializer_class  = CategorySerializer

	

	def get_queryset(self):
		return Category.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class CategoryDetail(generics.RetrieveAPIView):
	lookup_field		=	'title'
	serializer_class	=	CategorySerializer


	def get_queryset(self):
		return Category.objects.all()


	# def perform_update(self, serializer):
	# 	serializer.save(user = self.request.user)


	# def perform_delete(self, serializer):
	# 	serializer.save(user = self.request.user)

		

	
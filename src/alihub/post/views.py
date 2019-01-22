
from rest_framework import generics, mixins
from rest_framework.permissions import (
		IsAuthenticated,

	)
from .serializers import (

		PostSerializer,
		PostDetailSerializer,	
	)


from .models import Post
from .permissions import IsOwnerOrReadOnly








class PostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field      =  'id'
	serializer_class  = PostSerializer
	permission_classes = [IsOwnerOrReadOnly,]

	

	def get_queryset(self):
	
		return Post.objects.all()

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)




	



class PostRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	PostDetailSerializer
	permission_classes = [IsOwnerOrReadOnly,]

	def get_queryset(self):
		return Post.objects.all()

	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)




	


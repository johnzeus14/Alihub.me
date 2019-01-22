
from rest_framework import generics




from .serializers import CommentSerializer
from .models import Comment
from post.models import Post

from .permissions import IsOwnerOrReadOnly


class CommentAPIView(generics.ListCreateAPIView):
	lookup_field      =  'id'
	serializer_class  = CommentSerializer
	

	def get_queryset(self):
		return Comment.objects.all()


	def perform_create(self, serializer):
		serializer.save(user = self.request.user)


class CommentRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	CommentSerializer


	def get_queryset(self):
		return Comment.objects.all()


	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)

		

	
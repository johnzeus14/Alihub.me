
from rest_framework import generics, mixins
from rest_framework.permissions import (
		IsAuthenticated,

	)
from .serializers import (

		StorySerializer,
		StoryDetailSerializer,	
	)


from .models import Story
from .permissions import IsOwnerOrReadOnly








class StoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
	lookup_field      =  'id'
	serializer_class  = StorySerializer
	permission_classes = [IsOwnerOrReadOnly,]

	

	def get_queryset(self):
	
		return Story.objects.all()

	def perform_create(self, serializer):
		serializer.save(user = self.request.user)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)




	



class StoryRudView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field		=	'id'
	serializer_class	=	StoryDetailSerializer
	permission_classes = [IsOwnerOrReadOnly,]

	def get_queryset(self):
		return Story.objects.all()

	def perform_update(self, serializer):
		serializer.save(user = self.request.user)


	def perform_delete(self, serializer):
		serializer.save(user = self.request.user)




	


from rest_framework import generics
from posting.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .permission import IsOwnerOrReadOnly

class BlobPostAPIView(generics.ListCreateAPIView):
	queryset=BlogPost.objects.all()
	#query = self.request.GET.get('q')
	#if query is not None:
	#	queryset=queryset.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
	#return queryset
	serializer_class 	= BlogPostSerializer
	def perform_create(self,serializer):
		serializer.save(user=self.request.user)

class  BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
	queryset=BlogPost.objects.all()
	serializer_class 	= BlogPostSerializer
	lookup_field 	 = 'pk'
	permission_class	=[IsOwnerOrReadOnly]

	#def get_object(self):
	#	pk=self.kwargs.get('pk')
	#	return BlogPost.objects.get(pk=pk)

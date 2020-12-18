from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer): #forms.ModelForm
	class Meta:
		model=BlogPost
		fields ='__all__'
		read_only_fields=['user']

	#contverts to JSON
	#validations for data passed

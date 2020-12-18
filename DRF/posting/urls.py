from django.urls import path
from .views import BlogPostRudView,BlobPostAPIView
urlpatterns = [
	path('',BlobPostAPIView.as_view()),
    path('<int:pk>/', BlogPostRudView.as_view()),
]

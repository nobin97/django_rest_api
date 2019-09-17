from rest_framework.views import APIView
from .serializers import BlogSerializer
from .models import Blog
from rest_framework.response import Response
from rest_framework import status
from .forms import BlogForm


class BlogView(APIView):

    def get(self, request, pk=None):
        if not pk:
            try:
                blogs = Blog.objects.all()
                serializer = BlogSerializer(blogs, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                blog = Blog.objects.get(pk=pk)
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            except Blog.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        blog_form = BlogForm(request.data)
        if blog_form.is_valid():
            blog_form.save()

            return Response(status=status.HTTP_200_OK)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog_form = BlogForm(request.data, instance=blog)
            if blog_form.is_valid():
                blog_form.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)



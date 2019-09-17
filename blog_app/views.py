from rest_framework.views import APIView
from .serializers import BlogSerializer
from .models import Blog
from .forms import BlogForm
from utilities.mixins import ResponseViewMixin


class BlogView(APIView, ResponseViewMixin):

    def get(self, request, pk=None):
        if not pk:
            try:
                blogs = Blog.objects.all()
                serializer = BlogSerializer(blogs, many=True)
                data=serializer.data
                return self.success_response(
                    code='HTTP_200_OK',
                    data=data
                )
            except Exception as e:
                return self.error_response(
                    code='HTTP_500_INTERNAL_SERVER_ERROR',
                    message='An Unknown Exception Occurred.'
                )
        else:
            try:
                blog = Blog.objects.get(pk=pk)
                serializer = BlogSerializer(blog)
                data=serializer.data
                return self.success_response(
                    code='HTTP_200_OK',
                    data=data
                )
            except Exception as e:
                return self.error_response(
                    code='HTTP_500_INTERNAL_SERVER_ERROR',
                    message='An Unknown Exception Occurred.'
                )

    def post(self, request):
        try:
            blog_form = BlogForm(request.data)
            if blog_form.is_valid():
                blog_form.save()
                return self.success_response(
                    code='HTTP_200_OK'
                )
            return self.error_response(
                code='HTTP_400_BAD_REQUEST',
                message='Got Invalid Data'
            )
        except Exception as e:
            return self.error_response(
                code='HTTP_500_INTERNAL_SERVER_ERROR',
                message='An Unknown Exception Occurred.'
            )


    def put(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog_form = BlogForm(request.data, instance=blog)
            if blog_form.is_valid():
                blog_form.save()
                return self.success_response(
                    code='HTTP_200_OK'
                )
            return self.error_response(
                code='HTTP_400_BAD_REQUEST',
                message='Got Invalid Data'
            )
        except Exception as e:
            return self.error_response(
                code='HTTP_500_INTERNAL_SERVER_ERROR',
                message='An Unknown Exception Occurred.'
            )

    def delete(self, request, pk):
        try:
            blog = Blog.objects.get(pk=pk)
            blog.delete()
            return self.success_response(
                code='HTTP_204_NO_CONTENT'
            )
        except Exception as e:
            return self.error_response(
                code='HTTP_500_INTERNAL_SERVER_ERROR',
                message='An Unknown Exception Occurred.'
            )




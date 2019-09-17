from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.BlogView.as_view(), name='get_blog'),
    path('blogs/<int:pk>', views.BlogView.as_view(), name='get_blogs')
]
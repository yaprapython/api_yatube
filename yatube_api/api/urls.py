from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework.authtoken import views
from .views import GroupViewSet, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('posts/<int:post_id>/comments/',
         CommentViewSet.as_view(
             {'get': 'list',
              'post': 'create'}),
         name='comments'),
    path('posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view(
             {'get': 'retrieve',
              'put': 'update',
              'patch': 'partial_update',
              'delete': 'destroy'}),
         name='comment-detail'),
    path('', include(router.urls)),
]

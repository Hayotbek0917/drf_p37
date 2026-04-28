from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.serializers import PostModelSerializer
from apps.views import CustomTokenObtainPairView, PostModelViewSet

router = SimpleRouter(trailing_slash=False)
router.register('posts', PostModelViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    # path('posts', PostListCreateAPIView.as_view(), name='posts'),

]

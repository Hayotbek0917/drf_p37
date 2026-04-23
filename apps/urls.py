from django.urls import path

from apps.views import PostListCreateAPIView, CommentListAPIView, \
    PostRetrieveAPIView, AlbumListAPIView, PhotoListAPIView, PostRetrieveUpdateDestroyAPIView, PostCommentListAPIView, \
    UserListCreateAPIView, UserRetrieveAPIView, BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView, \
    StudentListCreateAPIView

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('books/', BookListCreateAPIView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', UserListCreateAPIView.as_view()),
    path('users/<str:username>', UserRetrieveAPIView.as_view()),
    path('posts/', PostListCreateAPIView.as_view()),
    # path('posts/<int:pk>/', PostRetrieveAPIView.as_view()),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<int:pk>/comments', PostCommentListAPIView.as_view()),
    path("comments/", CommentListAPIView.as_view()),
    path("albums", AlbumListAPIView.as_view()),
]
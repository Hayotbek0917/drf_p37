from django.db.models import Model
from django_filters import FilterSet, NumberFilter
from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema

from rest_framework.filters import SearchFilter, OrderingFilter

from apps.filters import PostFilter, AlbumFilter
from apps.serializers import PostModelSerializer, CommentModelSerializer, AlbumSerializer, PhotoSerializer, \
    UserModelSerializer, UserCreateModelSerializer, UserDetailModelSerializer, BookModelSerializer, \
    StudentModelSerializer

from apps.models import Post, Comment, Album, Photo, User, Book, Student

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView


@extend_schema(tags=['Student'])
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('age', 'created_at')

    def get_queryset(self):
        qs = super().get_queryset()

        name = self.request.query_params.get('name')
        grade = self.request.query_params.get('grade')
        min_age = self.request.query_params.get('min_age')
        active = self.request.query_params.get('active')

        if name:
            qs = qs.filter(name__icontains=name)
        if grade:
            qs = qs.filter(grade=grade)
        if min_age:
            qs = qs.filter(age__gte=min_age)
        if active is not None:
            if active.lower() == 'true':
                qs = qs.filter(is_active=True)
            elif active.lower() == 'false':
                qs = qs.filter(is_active=False)

        return qs


@extend_schema(tags=['Book'])
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ('title',)


@extend_schema(tags=['Book'])
class BookRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


@extend_schema(tags=['User'])
class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserCreateModelSerializer
        return super().get_serializer_class()


@extend_schema(tags=['User'])
class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.order_by('-id')
    serializer_class = UserDetailModelSerializer
    lookup_field = 'username'


@extend_schema(tags=['Post'])
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('userId',)
    # filterset_class = PostFilter


@extend_schema(tags=['Post'])
class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


@extend_schema(tags=['Post'])
class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


@extend_schema(tags=['Post'])
class PostCommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        pk = self.kwargs.get('pk')
        return qs.filter(postId=pk)


@extend_schema(tags=['Comment'])
class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter,)
    filterset_fields = ('postId', 'email')
    search_fields = ('email',)
    ordering_fields = ('id', 'postId', 'email')


@extend_schema(tags=['Album'])
class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('title', 'userId',)
    filterset_class = AlbumFilter


@extend_schema(tags=['Photo'])
class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

from django_filters import FilterSet, NumberFilter

from apps.models import Post, Album
from django.db.models import Count


class PostFilter(FilterSet):
    comment_count = NumberFilter(method='filter_comment_count')

    class Meta:
        model = Post
        fields = ()

    def filter_comment_count(self, queryset, key, value):
        return queryset.annotate(
            comment_count=Count('comments')
        ).filter(comment_count__gte=value)


# class PostFilter(FilterSet):
#     min_id = NumberFilter(field_name='id', lookup_expr='gte')
#     max_id = NumberFilter(field_name='id', lookup_expr='lte')
#
#     class Meta:
#         model = Post
#         fields = ('userId',)
#
#
class AlbumFilter(FilterSet):
    class Meta: 
        model = Album
        fields = ('userId',)

import datetime
from datetime import timedelta

from django.utils.timezone import now
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.models import Post, Comment, User, Album, Photo, Book, Student


class StudentModelSerializer(ModelSerializer):
    is_adult = SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'

    def validate_age(self, value):
        if value < 5:
            raise ValidationError('age 5 dan kichik bolmasin')
        return value

    def validate_grade(self, value):
        i = ['A', 'B', 'C']
        if value not in i:
            raise ValidationError("Grade faqat A, B, C bo'lishi kerak")
        return value

    def get_is_adult(self, i):
        return i.age >= 18


class BookModelSerializer(ModelSerializer):
    is_expensive = SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise ValidationError('Narxi 0 dan kichik bolishi mumkin emas')
        return value

    def validate_published_year(self, value):
        if value < 1900:
            raise ValidationError('1900 dan kichik bolmasin')
        return value

    def validate_custom(self, attrs):
        if attrs.get('title') == attrs.get('author'):
            raise ValidationError('Title abd Author bir xil bolishi mumkin emas')
        return attrs

    def get_is_expensive(self, i):
        return i.price > 100


class PostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = "__all__"


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


class UserCreateModelSerializer(ModelSerializer):
    confirm_password = CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'level': {'read_only': True}
        }

    def validate_username(self, val):
        if len(val) < 6:
            raise ValidationError('Username kamida 6 ta belgidan iborat bo`lishi shart!')
        return val

    def validate_first_name(self, val: str):
        if not val.lower().replace("g'", '').replace("o'", '').isalpha():
            raise ValidationError('Ism emasku bu!')
        return val

    def validate_phone(self, val: str):
        if val.startswith('+998'):
            return val.removeprefix('+998')
        return val

    def validate_birth_date(self, val):
        if now().year - val.year < 10:
            raise ValidationError('Foydalanuvchi 10 yoshdan katta bo`lishi shart!')
        return val

    def validate(self, attrs: dict):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if password != confirm_password:
            raise ValidationError('Parollar bir xil emas!')
        return attrs


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserListCreateModelSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = ('registered_at',)
        # read_only_fields = ('id', 'username', 'email', 'phone')
        extra_kwargs = {
            'password': {'write_only': True},
            'birth_date': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
            'address': {'write_only': True},
            'company': {'write_only': True},
            # 'registered_at': {'write_only': True},
        }

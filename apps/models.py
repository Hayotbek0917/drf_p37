from django.db.models import Model, IntegerField, CharField, TextField, URLField, ForeignKey, CASCADE, EmailField, \
    DateField, DecimalField, BooleanField
from django.db.models.fields import DateTimeField


class Post(Model):
    userId = IntegerField()
    title = CharField(max_length=255)
    body = TextField()
    created_at = DateTimeField(auto_now=True)


class Comment(Model):
    postId = ForeignKey("apps.Post", CASCADE)
    name = CharField(max_length=255)
    email = TextField()
    body = TextField()


class Album(Model):
    userId = IntegerField()
    title = CharField(max_length=255)


class Photo(Model):
    albumId = ForeignKey("apps.Album", CASCADE)
    title = CharField(max_length=255)
    url = URLField()
    thumbnailUrl = URLField()


class User(Model):
    username = CharField(max_length=255, unique=True)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255, null=True, blank=True)
    password = CharField(max_length=255)
    email = EmailField(max_length=255, null=True, blank=True)
    phone = CharField(max_length=15)
    address = CharField(max_length=255, null=True, blank=True)
    company = CharField(max_length=255, null=True, blank=True)
    birth_date = DateField(null=True, blank=True)
    registered_at = DateTimeField(auto_now=True)

class Book(Model):
    title = CharField(max_length=255)
    author = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    published_year = IntegerField()
    is_available = BooleanField(default=True)

class Student(Model):
    name = CharField(max_length=255)
    age = IntegerField()
    grade = CharField(max_length=255)
    is_active = BooleanField(default=True)
    created_at = DateTimeField(auto_now_add=True)

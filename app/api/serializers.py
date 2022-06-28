from rest_framework.serializers import ModelSerializer
from app.models import Author,Book


class AuthorSerializer(ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['name','email_id','phone_num']


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ['name','author','isbn_num','quantity','category','image']
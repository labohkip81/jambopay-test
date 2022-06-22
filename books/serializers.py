from rest_framework.serializers import ModelSerializer

from .models import Book, Author, Stock

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
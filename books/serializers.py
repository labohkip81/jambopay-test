from rest_framework.serializers import ModelSerializer

from .models import Book, Author, Stock


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class CreateStockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = ["book", "quantity"]


class StockHistorySerializer(ModelSerializer):
    class Meta:
        model = Stock.history.model
        fields = "__all__"

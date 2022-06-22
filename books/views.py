from .models import Book, Author, Stock
from .serializers import BookSerializer, AuthorSerializer, StockSerializer, CreateStockSerializer
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny


class BookViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    Create update and retrieve books
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)

class AuthorViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    Create update and retrieve authors
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (AllowAny,)
    

class StockViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    Create update and retrieve stocks
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (AllowAny,)
    

class CreateStockViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create stocks
    """

    queryset = Stock.objects.all()
    serializer_class = CreateStockSerializer
    permission_classes = (AllowAny,)
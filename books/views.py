from .models import Book, Author, Stock
from .serializers import BookSerializer
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

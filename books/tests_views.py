import json
import os

from django.test import TestCase, RequestFactory
from django.conf import settings
from bookstore.users.models import User
from rest_framework import status

from .views import BookViewSet, AuthorViewSet, StockViewSet, CreateStockViewSet
from .models import Book, Author, Stock

APP_DIR = os.path.dirname(os.path.abspath(__file__))


# Create your tests here.
class BookViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(
            id=1,
            first_name="test",
            last_name="test",
            email="test@gmail.com",
            date_of_birth="2022-06-22",
        )

    def test_book_list_returns_200_response(self):
        request = self.factory.get("api/v1/books/")
        response = BookViewSet.as_view({"get": "list"})(request).render()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK, "Book list view should return 200"
        )

    def test_book_create_returns_201_response(self):
        data = {
            "title": "Best Book",
            "author": 1,
            "year_of_publication": 2022,
            "description": "Test Description",
        }
        request = self.factory.post("api/v1/books/", data=data)
        response = BookViewSet.as_view({"post": "create"})(request).render()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            "Book create view should return 201",
        )


class AuthorViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_author_list_returns_200_response(self):
        request = self.factory.get("api/v1/authors/")
        response = AuthorViewSet.as_view({"get": "list"})(request).render()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Author list view should return 200",
        )

    def test_author_create_returns_201_response(self):

        data = {
            "first_name": "Laban",
            "last_name": "Kiplagat",
            "email": "labankiplagat81@gmail.com",
            "date_of_birth": "2020-03-04",
        }
        request = self.factory.post("api/v1/authors/", data=data)
        response = AuthorViewSet.as_view({"post": "create"})(request).render()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            "Author create view should return 201",
        )


class StockViewsTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.author = Author.objects.create(
            id=1,
            first_name="test",
            last_name="test",
            email="test@gmail.com",
            date_of_birth="2022-06-22",
        )
        self.book = Book.objects.create(
            title="Best Book",
            author=self.author,
            year_of_publication=2022,
            description="Test Description",
        )

    def test_stock_list_returns_200_response(self):
        request = self.factory.get("api/v1/stocks/")
        response = StockViewSet.as_view({"get": "list"})(request).render()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Stock list view should return 200",
        )

    def test_stock_create_returns_201_response(self):

        data = {
            "book": self.book.id,
            "quantity": 1,
        }
        request = self.factory.post("api/v1/stocks/create-stock/", data=data)
        response = CreateStockViewSet.as_view({"post": "create"})(request).render()
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            "Stock create view should return 201",
        )

    # def test_stock_patch_returns_200_response_and_updates_value(self):
    #     data = {
    #      "quantity": 10,
    #     }
    #     stock = Stock.objects.create(
    #         book = self.book,
    #         quantity = 1,)
    #     request = self.factory.patch(f"api/v1/stocks/{stock.id}/", data=data)
    #     response = StockViewSet.as_view({"patch": "partial_update"})(request, pk=stock.id).render()
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_200_OK,
    #         "Stock patch should return 200",
    #     )

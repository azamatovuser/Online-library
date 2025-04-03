from rest_framework import generics
from apps.book.serializers import BookSerializer
from apps.book.models import Book
from rest_framework.parsers import MultiPartParser, FormParser

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = (MultiPartParser, FormParser)


class BookDetailAPIView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
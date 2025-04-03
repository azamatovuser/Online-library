from django.urls import path
from apps.book.views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('all_books/', BookListCreateAPIView.as_view()),
    path('detail/<int:pk>/', BookDetailAPIView.as_view()),
]
from datetime import timedelta

from django.db.models import Q
from django.utils.timezone import now
from rest_framework import permissions, status
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from books.custom_permissions import IsLibrarianWithBookPermissions
from books.models import Book, Borrow
from books.serializers import BookSerializer, BorrowSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsLibrarianWithBookPermissions()]
        return [permissions.IsAuthenticated()]


class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        book = serializer.validated_data['book']
        if not book.available:
            raise serializers.ValidationError('Book not available')
        book.available = False
        book.save()
        serializer.save(user=self.request.user, due_date=now() + timedelta(days=14))

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(
                Q(book__title__icontains=search) |
                Q(book__author__icontains=search) |
                Q(book__genre__icontains=search)
            )
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return queryset

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        borrow = self.get_object()
        if borrow.returned:
            return Response({'detail': 'Book already returned.'}, status=status.HTTP_400_BAD_REQUEST)
        borrow.returned = True
        borrow.book.available = True
        borrow.book.save()
        borrow.save()
        return Response({'detail': 'Book returned successfully.'})

from rest_framework import serializers
from books.models import Book, Borrow


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'genre', 'available']

    def validate_title(self, value):
        if Book.objects.filter(title=value).exists():
            raise serializers.ValidationError("Book with this title already exists.")
        return value


class BorrowSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Borrow
        fields = ['id', 'book', 'user', 'borrow_date', 'returned']
        read_only_fields = ['user', 'borrow_date']

    # def get_book(self, obj):
    #     return obj.book.title

    def get_user(self, obj):
        return obj.user.name

from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from books.models import Book
from .models import User
from .validators import custom_password_validator


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[custom_password_validator]
    )

    class Meta:
        model = User
        fields = ["id", "name", "email", "password", "role"]

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.role == 'librarian':
            content_type = ContentType.objects.get_for_model(Book)
            permissions = Permission.objects.filter(
                content_type=content_type,
                codename__in=["add_book", "change_book", "delete_book"]
            )
            user.user_permissions.set(permissions)

        return user


class TokenObtainSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={"input_type": "password"})

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if not email or not password:
            raise serializers.ValidationError("Both email and password are required.")

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password.")

        return {"user": user}

from django.utils import timezone

from django.db import models

from accounts.models import User
from core.models import MasterModel


class Book(MasterModel):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now)
    due_date = models.DateTimeField()
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} - {self.user.name}"

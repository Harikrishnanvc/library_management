from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import BookViewSet, BorrowViewSet

router = DefaultRouter()
router.register(r'data', BookViewSet, basename='book')
router.register(r'borrows', BorrowViewSet, basename='borrow')

urlpatterns = [
    path("", include(router.urls)),

]

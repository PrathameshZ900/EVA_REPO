from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, LoginView, LogoutView,
    UserListCreateAPIView, AuthorViewSet, BooksViewSet, CountryViewSet
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BooksViewSet)
router.register(r'countries', CountryViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('', include(router.urls)),
]

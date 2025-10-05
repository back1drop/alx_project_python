from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend  # For filtering
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Review
from .serializers import ReviewSerializer, UserSerializer
from django.contrib.auth.models import User

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user  # Only owner can edit/delete

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set user on create

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  # Allow registration, but add auth for updates if needed

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        return super().get_permissions()

class MovieReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]  # Public read
    filter_backends = [OrderingFilter, DjangoFilterBackend]  # Sorting and filtering
    ordering_fields = ['rating', 'created_date']  # Sort options
    filterset_fields = ['rating']  # Filter by rating

    def get_queryset(self):
        movie_title = self.kwargs['movie_title']
        return Review.objects.filter(movie_title__iexact=movie_title)  # Case-insensitive filter

class ReviewSearchView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['movie_title', 'content']  # Search by title or content
    ordering_fields = ['rating', 'created_date']
    filterset_fields = ['rating']  # e.g., ?rating=4 or ?rating__gte=4 (using Django filters)

    def get_queryset(self):
        queryset = super().get_queryset()
        min_rating = self.request.query_params.get('min_rating')
        if min_rating:
            queryset = queryset.filter(rating__gte=min_rating)  # Custom filter example
        return queryset

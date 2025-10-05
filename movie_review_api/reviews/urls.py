from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, UserViewSet, MovieReviewsView, ReviewSearchView
from django.contrib.auth.views import LoginView, LogoutView
router = DefaultRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('movies/<str:movie_title>/reviews/', MovieReviewsView.as_view(), name='movie-reviews'),
    path('search/', ReviewSearchView.as_view(), name='review-search'),
    path('api/login/', LoginView.as_view(), name='login'), 
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
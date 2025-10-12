from django.urls import path
from .views import (
    register, login_view, logout_view, review_list, 
    create_review, update_review, delete_review
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('reviews/', review_list, name='review_list'),
    path('reviews/create/', create_review, name='create_review'),
    path('reviews/<int:pk>/update/', update_review, name='update_review'),
    path('reviews/<int:pk>/delete/', delete_review, name='delete_review'),
]
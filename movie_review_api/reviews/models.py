from django.db import models
from django.contrib.auth.models import User  # Using built-in User for CRUD
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Review(models.Model):
    movie_title = models.CharField(max_length=255)  # Movie title, allows duplicates
    content = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]  # 1-5 validation
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to user
    created_date = models.DateTimeField(default=timezone.now)  # Auto-set on create

    def __str__(self):
        return f"{self.movie_title} - {self.rating} by {self.user.username}"
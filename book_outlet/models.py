from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=50, null=True)
    is_bestseller = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.id])

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

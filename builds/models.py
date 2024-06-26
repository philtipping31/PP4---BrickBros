from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Choice Fields
BUILD_TYPES = (("Designed By Lego", "Designed By Lego"),
               ("Self Made", "Self Made"))

DIFFICULTY_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
    ('expert', 'Expert')
]


class Build(models.Model):
    """
    A model to create and manage lego build posts.
    """
    user = models.ForeignKey(
        User, related_name='build_owner', on_delete=models.CASCADE)
    build_title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    set_number = models.IntegerField()
    build_time = models.DurationField()
    build_type = models.CharField(
        max_length=50, choices=BUILD_TYPES, default="Designed By Lego")
    difficulty_rating = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default="easy")
    excerpt = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.build_title} | Posted by {self.user}"



class Review(models.Model):
    """
    A model to create the review option for build posts.
    """
    user = models.ForeignKey(
        User, related_name='review_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=False)
    build = models.ForeignKey(
        Build, related_name='build_post', on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    content = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-review_date"]

    def __str__(self):
        return f"{self.title} | Review added by {self.user}"
    
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField

# Create your models here.

# Choice Fields
BUILD_TYPES = (("designed_by_lego", "Designed By Lego"), ("selfmade", "Self Made"))

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
    user = models.ForeignKey(User, related_name='build_owner', on_delete=models.CASCADE)
    build_title = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, unique=True)
    image = ResizedImageField(
        size=[400, None], quality=75, upload_to='builds/', force_format='WEBP',
        blank=False, null=False
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)
    set_number = models.IntegerField()
    build_time = models.DurationField()
    build_type = models.CharField(max_length=50, choices=BUILD_TYPES, default="designed_by_lego")
    difficulty_rating = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="easy")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.build_title} | Posted by {self.user}"



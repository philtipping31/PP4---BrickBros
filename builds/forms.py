from django import forms
from .models import Build, Review


class BuildForm(forms.ModelForm):
    """
    A form for creating and updating lego build posts.

    """
    class Meta:
        model = Build
        fields = ['build_title', 'slug', 'image', 'image_alt',
                  'set_number', 'build_time', 'build_type',
                  'difficulty_rating', 'excerpt', 'content']
        labels = {
            'build_title': "Build Title",
            'slug': "Slug (Title lowercase, and spaces replaced with '-')",
            'image': "Build Image",
            'image_alt': "Describe Image",
            'set_number': "Model Number",
            'build_time': "Build Time (Minutes)",
            'build_type': "Build Type",
            "difficulty_rating": "Build Difficulty",
            "excerpt": "Short Description",
            "content": "Write something about the build"
        }


class ReviewForm(forms.ModelForm):
    """
    A form for adding a review to a build post.
    """
    class Meta:
        model = Review
        fields = ['title', 'content', 'rating']
        labels = {
            'content': "Add your review here",
            'rating': "Rating out of 5 stars"
        }
        RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
        widgets = {'rating': forms.Select(choices=RATING_CHOICES)}

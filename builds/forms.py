from django import forms
from .models import Build


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

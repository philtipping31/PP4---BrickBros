from django import forms
from .models import Build


class BuildForm(forms.ModelForm):
    """
    A form to add a lego build.
    """
    class Meta:
        model = Build
        fields = ['build_title', 'image', 'set_number', 'build_time', 'build_type', 'difficulty_rating', 'content']
        labels = {
            'build_title': "Build Title",
            'image': "Build Image",
            'set_number': "Model Number",
            'build_time': "Build Time (Minutes)",
            'build_type': "Build Type",
            "difficulty_rating": "Build Difficulty",
            "content": "Write something about the build"
        }

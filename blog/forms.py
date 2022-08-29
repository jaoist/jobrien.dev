from django import forms

from pagedown.widgets import AdminPagedownWidget

from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())

    class Meta:
        model = BlogPost
        fields = "__all__"
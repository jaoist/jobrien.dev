from django import forms
from django.contrib import admin
from .forms import BlogPostForm
from .models import BlogPost

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = BlogPost
#         fields = "__all__"
    
#     content = forms.CharField(widget=forms.Textarea)

# Register your models here.
# class BlogPostAdmin(admin.ModelAdmin):
#     form = BlogPostForm

class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm

admin.site.register(BlogPost, BlogPostAdmin)


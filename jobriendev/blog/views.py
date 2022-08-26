from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import BlogPost

# A view has one job: Return a response. Or a 404.

# Create your views here.
class IndexView(ListView):
    # The context_object_name is the name of the object that takes the return of the get or post method
    context_object_name = 'blog_posts' 
    template_name = 'blog/index.html'

    def get_queryset(self):
        """
        Return blog posts ordered by publish date. This will allow displaying
        the latest post by indexing the first item.
        """
        blog_posts = BlogPost.objects.all().order_by('-pub_date')
        return blog_posts

class DetailView(DetailView):    
    template_name = "blog/detail.html"
    model = BlogPost

    # This method creates a context dictionary.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_count"] = BlogPost.objects.count()
        return context
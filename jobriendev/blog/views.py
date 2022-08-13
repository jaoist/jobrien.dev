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
        return BlogPost.objects.all().order_by('-pub_date')

class DetailView(DetailView):
    
    model = BlogPost
    template_name = "blog/detail.html"
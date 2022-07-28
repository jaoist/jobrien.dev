import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import BlogPost

# A view has one job it has to do: Return a response. Or a 404.

# Create your views here.
class IndexView(generic.ListView):
    # The context_object_name is the name of the object that takes the return of the get or post method
    context_object_name = 'blog_posts' 
    template_name = 'blog/index.html'

    def get_queryset(self):
        return BlogPost.objects.all()


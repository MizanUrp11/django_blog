from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog
# Create your views here.

class HomePageView(ListView):
    model = Blog
    template_name = 'home.html'
    context_object_name = 'all_blogs_from_posts'
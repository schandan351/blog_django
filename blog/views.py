from django.shortcuts import render
from  .models import Post
from django.views.generic import ListView,DetailView
# Create your views here.

class ShowPosts(ListView):
  model=Post


class ShowDetail(DetailView):
  model=Post
  template_name='blog/post_detail.html'
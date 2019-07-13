from django.shortcuts import render
from  .models import Post,Comment
from django.views.generic import ListView,DetailView,TemplateView
# Create your views here.

class ShowPosts(ListView):
  model=Post


class ShowDetail(DetailView):
  model=Post
  template_name='blog/post_detail.html'

class ShowComment(TemplateView):
  model=Comment
  template_name='blog/post_detail.html'
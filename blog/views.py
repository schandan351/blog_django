from django.shortcuts import render,HttpResponseRedirect,HttpResponse,get_object_or_404
from  .models import Post,Comment
from django.views.generic import ListView,DetailView,TemplateView,CreateView,FormView
from django.views import View
from blog.forms import CommentForm
# Create your views here.

class ShowPosts(ListView):
  model=Post

class ShowDetail(DetailView):
  model=Post
  template_name='blog/post_detail.html'


class ShowComment(TemplateView):
  model=Comment
  template_name='blog/post_detail.html'

class CommentForms(FormView):
  template_name='blog/post_detail.html'
  form_class=CommentForm
  success_url='/'

  def form_valid(self,form):
    form.save()
    return HttpResponse("Thanks")


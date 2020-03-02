from django.shortcuts import render,redirect
from django.utils import timezone
from app.forms import PostForm,HostelForm,ProblemForm
from django.views.generic import (TemplateView,ListView,DeleteView,DetailView,CreateView,UpdateView)
from django.urls import reverse_lazy
from app.models import Post,Hostel,Problem

# Create your views here.

class PostListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(create_date__lte=timezone.now()).order_by('create_date')

class PostDetailView(DetailView):
    model=Post

class CreatePostView(CreateView):
    redirect_field_name='app/post_detail.html'
    form_class=PostForm
    model=Post

class PostUpdateView(UpdateView):
    redirect_field_name='app/post_detail.html'
    form_class=PostForm
    model=Post

class PostDeleteView(DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')



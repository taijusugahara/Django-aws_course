from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index(request):
  posts = Post.objects.order_by('-published').all()
  return render(request,'index.html', context={
    'posts' : posts
  })

def post_detail(request,post_id):
  post = get_object_or_404(Post, pk=post_id)
  return render(request,'post_detail.html', context={
    'post' : post
  })
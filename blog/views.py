from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html',
                  {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html'
                  , {'post': post})
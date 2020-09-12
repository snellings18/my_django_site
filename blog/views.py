from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(requests):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(requests, 'blog/post_list.html', stuff_for_frontend)

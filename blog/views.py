from datetime import datetime
from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post, Comment, Category
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.all().filter(published=True)
    category = Category.objects.all()
    counter = posts.count()
    context = {'items': posts, 'category': category, 'counter': counter}
    return render(request, 'blog/post_list.html', context)

def categories(request, category_pk):
    posts = Post.objects.filter(category=category_pk)
    catogory = Category.objects.all()
    counter = posts.count()
    return render(request, 'blog/post_list.html', {'items': posts, 'category': catogory, 'counter': counter})

def post_draft(request):
    posts = Post.objects.all().filter(published=False)
    context = {'items': posts}
    return render(request, 'blog/post_list.html', context)

def published_post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.published = True
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post}) 

def post_detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment = Comment.objects.filter(post = post_pk)
    counter = comment.count()
    context = {'post': post, 'comment': comment, 'counter': counter}
    return render(request, 'blog/post_detail.html', context)

def post_new(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)

def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)

def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk).delete()
    return redirect('post_list')


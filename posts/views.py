from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, 'posts/post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # Добавляем обработку файлов
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
            form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.is_staff and post.author != request.user:
            raise PermissionDenied
    post.delete()
    return redirect('post_list')

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    return redirect('post_detail', pk=pk)

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_id = comment.post.id
    if not request.user.is_staff and comment.author != request.user:
        raise PermissionDenied
    comment.delete()
    return redirect('post_detail', pk=post_id)

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from blogs.forms import BlogForm, BlogCommentForm
from blogs.models import Blog, BlogPost


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'blogs/index.html')

@login_required
def all_blogs(request: HttpRequest) -> HttpResponse:
    """Возвращает список тем блога"""
    if request.user.is_authenticated:
        all_blogs = Blog.objects.filter(owner=request.user).order_by('-date_added')
        context = {'all_blogs': all_blogs}
        return render(request, 'blogs/all_blogs.html', context)
    else:
        return render(request, 'registration/login.html')


@login_required
def blog(request: HttpRequest, blog_id: int) -> HttpResponse:
    blog = get_object_or_404(Blog, id=blog_id)
    text_blog = blog.blog_posts.order_by('-date_added')
    context = {
        'blog': blog,
        'text_blog': text_blog
    }
    return render(request, 'blogs/blog.html', context)


@login_required
def add_blog(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect(reverse_lazy('blogs:all_blogs'))
    context = {'form': form}
    return render(request, 'blogs/add_blog.html', context)


@login_required
def new_post(request: HttpRequest, blog_id: int) -> HttpResponse:
    blog = get_object_or_404(Blog, id=blog_id)
    check_owner(request.user, blog)
    if request.method != 'POST':
        form = BlogCommentForm()
    else:
        form = BlogCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.title = blog
            new_comment.save()
            return redirect('blogs:blog', blog_id=blog_id)
    context = {
        'blog': blog,
        'form': form,
    }
    return render(request, 'blogs/new_post.html', context)


@login_required
def edit_post(request: HttpRequest, post_id: int) -> HttpResponse:
    text = get_object_or_404(BlogPost, id=post_id)
    title_blog = text.title
    check_owner(request.user, title_blog)
    if request.method != 'POST':
        form = BlogCommentForm(instance=text)
    else:
        form = BlogCommentForm(instance=text, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('blogs:blog', kwargs={'blog_id': title_blog.id}))
    context = {
        'text': text,
        'title_blog': title_blog,
        'form': form,
    }
    return render(request, 'blogs/edit_post.html', context)


def check_owner(user, blog):
    if user != blog.owner:
        raise Http404

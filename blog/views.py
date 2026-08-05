from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


# Home Page
def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {
        'blogs': blogs
    })


# Blog Detail Page
def detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'detail.html', {
        'blog': blog
    })


# Create Blog
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {
        'form': form
    })


# Edit Blog
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'create_blog.html', {
        'form': form
    })


# Delete Blog
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if request.method == 'POST':
        blog.delete()
        return redirect('home')

    return render(request, 'delete_blog.html', {
        'blog': blog
    })
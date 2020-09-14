from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comments, Category
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from . import forms
from django.core.mail import send_mail
from .models import CustomTag
from django.contrib.auth.models import User
from user_profile.models import UserProfile


# def blog(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/detail.html', {'posts': posts})

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'

def get_all_categories():
    return Category.objects.all()

def get_three_latest_posts():
    return Post.published.filter()[0:3]

def get_all_tags():
    return Post.tags.all()

def single_post(request):
    return render(request, 'blog/detail.html')

def post_list(request, tag_slug=None, category_slug=None):
    object_list = Post.published.all()
    latest_posts = object_list[:3]

    # username = None
    # if user_name:
    #     username = get_object_or_404(User, slug=user_name)
    #     object_list = object_list.filter(user=request.user)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(category__in=[category])

    tag = None
    if tag_slug:
        tag = get_object_or_404(CustomTag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, 1) # 3 posts in each page
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/list.html', {'posts': posts, 'tag': tag, 'category': category, 'three_latest_posts': latest_posts, 'tags': get_all_tags(), 'categories': get_all_categories()})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='منتشر شده',
                               publish__year=year, publish__month=month,
                               publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    
    new_comment = None

    if request.method == 'POST': 
        comment_form = forms.CommentsForm(request.POST)
        if comment_form.is_valid():
            # Create comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.user = request.user
            new_comment.save()
    else:
        comment_form = forms.CommentsForm()
    return render(request, 'blog/detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form, 'three_latest_posts': get_three_latest_posts(), 'tags': get_all_tags(), 'categories': get_all_categories()})

    


from .models import Profile, Post
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import CreatePost
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    context = {
        "users": User.objects.all(),
        "profiles": Profile.objects.all()
    }
    return render(request, 'main/home.html', {"context": context})

@login_required
def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    is_following = profile.is_followed_by(request.user)
    author = User.objects.get(username = username)
    
    context = {
        'profile': profile,
        'is_following': is_following,
        'author': author
    }
    return render(request, 'users/profile.html', context)

@login_required
def follow_toggle(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=profile_id)
        
        # Don't allow users to follow themselves
        if request.user == profile.user:
            return JsonResponse({'status': 'error', 'message': 'You cannot follow yourself'})
        
        # Toggle follow status
        if profile.is_followed_by(request.user):
            profile.followers.remove(request.user)
            is_following = False
        else:
            profile.followers.add(request.user)
            is_following = True
            
        return JsonResponse({
            'status': 'success',
            'is_following': is_following,
            'followers_count': profile.get_followers_count()
        })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def post(request, username, post_id):
    author = User.objects.get(username = username)
    post = author.post_set.get(id = post_id)
    comment = ''
    context = {
        "author": author,
        "post": post,
        "comment": comment
    }
    return render(request, 'main/post.html', context)

def create(request):
    author = request.user
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            post = Post(author = author, title = title, text = text)
            post.save()
    else:
        form = CreatePost()
    return render(request, 'main/create.html', {"form": form})
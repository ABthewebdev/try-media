from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})

@login_required
def profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    is_following = profile.is_followed_by(request.user)
    
    context = {
        'profile': profile,
        'is_following': is_following,
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
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    picture = models.ImageField(upload_to="profile_pics", default="default_picture.jpg")

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    def get_followers_count(self):
        return self.followers.count()
    
    def get_following_count(self):
        return Profile.objects.filter(followers=self.user).count()
    
    def is_followed_by(self, user):
        return user in self.followers.all()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=500)
    likes = models.ManyToManyField(User, related_name='liked', blank=True)
    imageSrc = models.CharField(max_length=255, default=None, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def get_likes(self):
        return self.likes.count()
    
    def get_comments(self):
        return self.comments.count()
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.author.username} commented"
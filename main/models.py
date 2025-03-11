from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

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
    comments = models.ManyToManyField(User, related_name='commented', blank=True)

    def likes_post(self):
        return f"{self.author.username} likes this post"
    
    def get_likes(self):
        return Post.objects.filter(likes=self.user).count()
    
    def get_comments(self):
        return self.comments.count()
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.author.username} commented"
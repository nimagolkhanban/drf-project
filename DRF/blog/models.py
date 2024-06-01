from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    # tip: by implimenting this in the code if you want to query any data in the model it
    # will show you the data with published status in it
    class PostObjects(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset().filter(status="published")
        
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    
    Category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    status = models.CharField(
        max_length=10, choices=options, default='published'
    )
    
    class Meta:
        ordering = ['-published']
        
    def __str__(self) -> str:
        return self.title
    
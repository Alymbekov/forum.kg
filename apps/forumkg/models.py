import os
import random
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.category.models import Category


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    print('base_name', base_name)
    name, ext = os.path.splitext(base_name)
    print(name, ext)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3999999999)
    print("newfilename", new_filename)
    name, ext = get_filename_ext(filename)
    print(name, ext)
    final_filename = f'{new_filename}{ext}'
    print('final_filename', final_filename)
    return f'post_images/{new_filename}/{final_filename}'

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
        )
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='category_posts'
    )
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft'
        )
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title
    
class PostImage(models.Model):
    image = models.ImageField(upload_to=upload_image_path)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='images'
    )

    def __str__(self):
        return f'{self.post.title}.jpg'
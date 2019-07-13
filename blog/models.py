from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
  title=models.CharField(max_length=100)
  detail=models.TextField()
  image=models.ImageField(upload_to='image/',blank=True)
  author=models.CharField(max_length=100)
  draft=models.BooleanField(default=True)
  published_date=models.DateTimeField(auto_now_add=True)

  def __str_(self):
    return self.title

  def get_absolute_url(self):
    return reverse('post_detail',kwargs={'pk':self.pk})

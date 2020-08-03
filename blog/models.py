from django.db import models
# Create your models here.
from django.db import models


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    post = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()

#create migrations
python manage.py makemigrations

#run migrations
python manage.py migrate


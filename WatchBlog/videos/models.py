from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rate = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    TYPES_VIDEOS = [
        ('Film', 'Film'),
        ('Serie', 'Serie')
    ]
    types_videos = models.CharField(
        max_length = 10,
        choices = TYPES_VIDEOS,
        default = 'Film'
    )
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

User = get_user_model()

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    rate = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['gif','png','jpg'])])

    TYPES_VIDEOS = [
        ('Film', 'Film'),
        ('Serie', 'Serie')
    ]
    type_video = models.CharField(
        max_length = 10,
        choices = TYPES_VIDEOS,
        default = 'Film'
    )

    CATEGORIES_VIDEOS = [
        ('Animation', 'Animation'),
        ('Biopic', 'Biopic'),
        ('Comédie', 'Comédie'),
        ('Documentaire', 'Documentaire'),
        ('Drame', 'Drame'),
        ('Fantastique', 'Fantastique'),
        ('Science-fiction', 'Science-fiction'),
        ('Horreur', 'Horreur'),
        ('Guerre', 'Guerre'),
        ('Histoire', 'Biopic'),
        ('Policier', 'Policier'),
        ('Thriller', 'Thriller'),
        ('Aventure', 'Aventure')
    ]
    category_video = models.CharField(
        max_length = 50,
        choices = CATEGORIES_VIDEOS,
        default = 'Animation'
    )

    def __str__(self):
        return self.title
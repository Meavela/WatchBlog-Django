# Generated by Django 2.2.9 on 2020-01-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_auto_20200118_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='category_video',
            field=models.CharField(choices=[('Animation', 'Animation'), ('Biopic', 'Biopic'), ('Comédie', 'Comédie'), ('Documentaire', 'Documentaire'), ('Drame', 'Drame'), ('Fantastique', 'Fantastique'), ('Science-fiction', 'Science-fiction'), ('Horreur', 'Horreur'), ('Guerre', 'Guerre'), ('Histoire', 'Biopic'), ('Policier', 'Policier'), ('Thriller', 'Thriller'), ('Aventure', 'Aventure')], default='Animation', max_length=50),
        ),
    ]

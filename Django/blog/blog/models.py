from django.db import models

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

class Artist(models.Model):
    name= models.CharField(max_length=200, db_index=True, help_text='Artist name')

    def __str__(self):
        """String for representing the Model object"""
        return self.name

class Album(models.Model):
    title= models.CharField(max_length=200, db_index=True, help_text='Album title')
    artist= models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object"""
        return self.title

class Genre(models.Model):
    name= models.CharField(max_length=200, db_index=True, help_text='Genre of music (i.e. Blues)')

    def __str__(self):
        """String for representing the Model object"""
        return self.name
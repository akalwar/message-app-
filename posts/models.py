from django.db import models

# Creating first model for app posts

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        '''Representation of model in string form'''
        return self.text[:50]




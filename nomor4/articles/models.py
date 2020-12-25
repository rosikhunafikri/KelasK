from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title

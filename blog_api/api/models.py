from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    age = models.SmallIntegerField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=180)
    def __str__(self):
        return self.title
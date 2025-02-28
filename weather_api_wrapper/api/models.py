from django.db import models

class Requests(models.Model):
    request = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request[:15]
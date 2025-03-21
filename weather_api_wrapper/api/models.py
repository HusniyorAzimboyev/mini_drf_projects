from django.db import models

class Requests_data(models.Model):
    request = models.CharField(max_length=1000)
    response = models.CharField(max_length=1000)
    data_from_api = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{str(self.created_at)[:16]} - {self.request.split('/')[::-1][0]}'

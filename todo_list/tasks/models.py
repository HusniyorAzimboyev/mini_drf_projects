from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    statusChoices = (
        (1,1),
        (0,0)
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(choices=statusChoices) # 0 means not done, 1 means done.
    def __str__(self):
        return f"{self.user.username}'s - {self.title}"

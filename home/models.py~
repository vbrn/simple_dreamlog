from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dreams_log(models.Model):
    title = models.CharField(max_length=3000)
    content = models.TextField()
    rating = models.IntegerField(default = 0)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Сонник"
        verbose_name_plural = "Сонник"
    

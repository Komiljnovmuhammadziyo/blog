from django.db import models

from users.models import CustomUser

class Islam(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=250)
    body = models.TextField()
    image = models.ImageField(upload_to='media-files/', blank=True, null=True)  # Correcting the upload_to path
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def __str__(self):
        return f"{self.name} - {self.body[:50]}"



class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    islam = models.ForeignKey(Islam, on_delete=models.CASCADE)
    body = models.TextField()
    questions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('game-detail', kwargs={'pk': self.pk})
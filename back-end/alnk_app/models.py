from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    owner = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    original_link = models.URLField(null=False)
    shortened_link = models.URLField(null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date_created)
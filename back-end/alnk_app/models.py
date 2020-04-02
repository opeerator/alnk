from django.db import models
from django.contrib.auth.models import User
import datetime


class Link(models.Model):
    owner = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    original_link = models.URLField(null=False)
    shortened_link = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.owner.username)


class LinkView(models.Model):
    requestor_link = models.ForeignKey(Link, on_delete=models.CASCADE)
    requestor_ip = models.GenericIPAddressField()
    requestor_connection = models.TextChoices('Proxy', 'Real')
    requestor_identity = models.TextChoices('Bot', 'Real')
    requestor_os = models.TextField(max_length=80)
    request_time = models.DateTimeField(auto_now_add=datetime.datetime.now())


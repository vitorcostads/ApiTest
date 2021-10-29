from django.db import models
from uuid import uuid4

class movies(models.Model):
    id_movie = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release = models.IntegerField()
    duration = models.IntegerField()
    creat_at = models.DateField(auto_now_add=True)






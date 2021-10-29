from django.db import models
from client.models import client
from movies.models import movies


class rent(models.Model):
    id_rent = models.AutoField(primary_key= True, editable=False)
    recieve = models.DateTimeField(blank= False, null= False)
    regress = models.DateTimeField(blank= False, null= False)
    note = models.TextField(max_length=255, blank=True, null=True)
    client = models.ForeignKey(client, on_delete=models.CASCADE, related_name= 'Rents',blank= False, null= False )
    movies = models.ForeignKey(movies, on_delete=models.CASCADE, related_name= 'Movie',blank= False, null= False  )

    class Meta:
        managed = True
        db_table = 'Rent'
        unique_together = ('client', 'movies')
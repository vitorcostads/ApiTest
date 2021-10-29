from django.db import models

class client(models.Model):
    id_client = models.AutoField(primary_key=True, editable=False)
    CPF = models.CharField(max_length=15)
    name = models.CharField(max_length=90)
    birthday = models.DateField(blank=True, null=True)
    adress = models.CharField(max_length=150, blank=True, null=True)
    number_adress = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Client'


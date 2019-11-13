from django.db import models

# Create your models here.
class Emp(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)

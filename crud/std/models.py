from django.db import models

# Create your models here.
class Books(models.Model):
    idn=models.CharField(max_length=100,null= False)
    name=models.CharField(max_length=100,null=False)
    rName=models.CharField(max_length=100,null=True)
    rAge=models.IntegerField(null=True)
    page=models.IntegerField(null=True)
    date=models.DateField(null=True)
    type=models.CharField(max_length=100,null= True)
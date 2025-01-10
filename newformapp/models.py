from django.db import models

# Create your models here.
class mydetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    age=models.IntegerField()
    adress=models.CharField(max_length=200)
    phonenumber=models.IntegerField()

    def __str__(self):
        return self.name

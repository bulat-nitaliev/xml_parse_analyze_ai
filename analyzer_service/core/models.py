from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):...

class Product(models.Model):
    prod_id = models.IntegerField()
    name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=150)
    date_product = models.DateField()

    def __str__(self):
        return self.name
    
class AnswerLLm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.TextField()
    answer = models.TextField()
    dt_create = models.DateTimeField(auto_now_add=True)


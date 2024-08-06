from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    user_id = models.IntegerField()
    plaid_info = models.TextField()
    coinbase_info = models.TextField()


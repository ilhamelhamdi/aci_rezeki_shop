from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    id = models.AutoField(primary_key=True)
    price = models.IntegerField()
    image = models.URLField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Item - {self.id} - {self.name}"
    

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Category - {self.id} - {self.name}"
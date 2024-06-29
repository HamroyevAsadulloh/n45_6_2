from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100),
    description = models.TextField()
    author = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    price = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description



class Authors(models.Model):
    name = models.CharField(max_length=25)
    age = models.PositiveIntegerField()
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name

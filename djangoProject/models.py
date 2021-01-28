from django.db import models


# create models here


class User(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Subject = models.CharField(max_length=200)
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.Name + self.Email + self.Subject + self.Message

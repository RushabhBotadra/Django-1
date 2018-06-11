from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=1000)
    price = models.IntegerField()


    def __str__(self):
        return self.name


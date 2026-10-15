from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Local"
        verbose_name_plural = "Locais"

    def __str__(self):
        return self.name

    
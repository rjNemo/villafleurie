from django.db import models



class Guest(models.Model):
    class Meta:
        verbose_name = "Voyageur"

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=30, blank=True)

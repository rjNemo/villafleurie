from django.db import models


class Picture(models.Model):
    def __str__(self):
        return self.alt

    img = models.ImageField(upload_to='img/', null=True, blank=True)
    alt = models.CharField(max_length=100)

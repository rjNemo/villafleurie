from django.db import models



class Contact(models.Model):

    def __str__(self):
        return f"Message de {self.name}, le {self.date}"

    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.EmailField(max_length=50)
    message = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

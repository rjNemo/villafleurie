from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Place(models.Model):
    class Meta:
        verbose_name = "Appartement"

    def __str__(self):
        return self.name

    name=models.CharField(max_length=10, unique=True)
    pictures=models.ImageField(upload_to="uploads/",null=True,blank=True)
    description=models.TextField(blank=True)
    subname=models.CharField(max_length=100, blank=True)
    tagline=models.CharField(max_length=100, blank=True)
    price=models.DecimalField(max_digits=6, decimal_places=2, null=True)


class Guest(models.Model):
    class Meta:
        verbose_name = "Voyageur"

    def __str__(self):
        return self.name

    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone=PhoneNumberField(blank=True)


class Reservation(models.Model):
    class Meta:
        verbose_name = 'Réservation'

    def __str__(self):
        return "Réservation du {} par {}".format(self.place, self.guest)

    place=models.OneToOneField(Place,on_delete=models.CASCADE)
    guest=models.ForeignKey(Guest,on_delete=models.CASCADE)


class Testimonial(models.Model):
    class Meta:
        verbose_name="Témoignage"

    def __str__(self):
        return self.title

    title=models.CharField(max_length=100)
    reservation=models.OneToOneField(Reservation,on_delete=models.CASCADE)
    text=models.TextField()

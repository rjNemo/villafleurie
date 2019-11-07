from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from villafleurie import settings

class Place(models.Model):
    class Meta:
        verbose_name = "Appartement"

    def __str__(self):
        return self.name

    name=models.CharField(max_length=10, unique=True)
    pictures=models.ImageField(upload_to="img/",null=True,blank=True)
    description=models.TextField(blank=True)
    info=models.TextField(blank=True)
    subname=models.CharField(max_length=100, blank=True)
    tagline=models.CharField(max_length=100, blank=True)
    price=models.DecimalField(max_digits=6, decimal_places=2, null=True)
    surface=models.IntegerField(null=True,blank=True)
    beds=models.IntegerField(null=True,blank=True)
    max_occupation=models.IntegerField(null=True,blank=True)


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
    message=models.TextField(blank=True)


class Testimonial(models.Model):
    class Meta:
        verbose_name="Témoignage"

    def __str__(self):
        return self.author

    author=models.CharField(max_length=100)
    text=models.TextField()
    picture=models.ImageField(upload_to='img/',null=True,blank=True)
    link=models.URLField(null=True,blank=True)
    guest=models.OneToOneField(Guest,on_delete=models.CASCADE,blank=True,null=True)
    reservation=models.OneToOneField(Reservation,on_delete=models.CASCADE,blank=True,null=True)

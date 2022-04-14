from django.db import models

# Create your models here.


class Booking(models.Model):
    pet_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    owner_phone_number = models.CharField(max_length=200)
    grooming_package = models.CharField(max_length=200)
    grooming_session = models.DateTimeField('Date Booking and Time')



def _str_(self):
    return self.text



from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Address(models.Model):
    TYPES = (
        ('home', _('home')),
        ('office', _('office')),
        ('other', _('other'),)
    )
    address_type = models.CharField(choices=TYPES, max_length=10)
    street_address = models.TextField(max_length=200)
    pincode = models.PositiveIntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=50)

    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    def __latitude__(self):
        return self.latitude

    def __longitude__(self):
        return self.longitude

    def __str__(self):

        return self.pincode

    class Meta:
        verbose_name_plural = 'Addresses'


class Customer(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=120)
    email = models.EmailField(_('email_address'), unique=True)
    phonenumber = models.PositiveIntegerField(
        _('phone_number'), unique=True, max_length=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
    )
    gender=models.CharField(choices=GENDER_CHOICES,default=GENDER_CHOICES[0],max_length=20)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



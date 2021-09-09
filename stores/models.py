
from django.db import models
from django.utils.translation import ugettext_lazy as _
from accounts.models import Customer, Address
#  Create your models here.


class Rider(models.Model):
    name = models.CharField(_('name'), unique=True, max_length=120)
    email = models.EmailField(_('email_address'), unique=True)
    phonenumber = models.PositiveIntegerField(
        _('phone_number'), unique=True, max_length=10)
    member_since = models.DurationField()
    online = models.BooleanField(default=False)

    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)

    order_delivered = models.PositiveIntegerField(default=1379)
    RATE_CHOICES = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'),
    )
    average_rating = models.PositiveSmallIntegerField(_('rating'),
                                                      choices=RATE_CHOICES, default=RATE_CHOICES[0])

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(_('title'), max_length=200, unique=True)
    description = models.TextField(_('description'), max_length=300)
    url = models.TextField(_('url'), max_length=600)
    price = models.FloatField(_('price'))
    popular = models.BooleanField(_('popular'))

    def __str__(self):
        return self.title


class Store(models.Model):
    store_name = models.CharField(_('name'), max_length=100, unique=True)
    STORE_CATEGORY = (
        ('K', 'Kirana Store'),
        ('S', 'SuperMarket')
    )
    store_category = models.CharField(
        _('category'), choices=STORE_CATEGORY, max_length=10, default=STORE_CATEGORY[0])

    street_address = models.TextField(
        _('address'), max_length=300, unique=False,)
    pincode = models.PositiveIntegerField(_('pincode'), max_length=6)

    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longitude = models.DecimalField(max_digits=15, decimal_places=10)
    products = models.ManyToManyField(Product)

    RATE_CHOICES = (
        (1, 'One Star'),
        (2, 'Two Star'),
        (3, 'Three Star'),
        (4, 'Four Star'),
        (5, 'Five Star'),
    )
    average_rating = models.PositiveSmallIntegerField(_('rating'),
                                                      choices=RATE_CHOICES, default=RATE_CHOICES[0])
    average_packaging_time = models.PositiveIntegerField(
        _('packaging_time'), default=30)

    def __str__(self):
        return self.store_name



'''

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_option = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
'''
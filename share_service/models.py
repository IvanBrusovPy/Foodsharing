from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=30)


class Customer(models.Model):
    phone = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Cafe(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Offer(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    book_time = models.TimeField()
    pick_up_time = models.TimeField()
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(default="In progress", max_length=20)
    total = models.CharField(max_length=3)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.total = str(self.quantity*self.offer.price)





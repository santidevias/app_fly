from django.db import models
from django.contrib.auth.models import User


class Fly(models.Model):

    name = models.CharField(max_length=30)
    code_airline = models.CharField(max_length=30)


class OrderReservation(models.Model):

    code_order = models.CharField(max_length=10)


class FlyReservation(models.Model):

    fists_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    second_last_name = models.CharField(max_length=30)
    date_start = models.DateTimeField(blank=False, null=False)
    date_end = models.DateTimeField(blank=True, null=True)
    fly_id = models.ForeignKey(Fly, on_delete=models.CASCADE)
    order_id = models.ForeignKey(OrderReservation, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    

class TickeService(models.Model):

    status_pay = models.BooleanField(default=True)
    fly_reservation = models.OneToOneField(FlyReservation, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

# Create your models here.

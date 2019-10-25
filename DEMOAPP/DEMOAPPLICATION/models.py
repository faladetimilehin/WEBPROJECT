from django.db import models
from datetime import datetime


# Create your models here.
class Officer(models.Model):
    officer_fname = models.CharField(max_length=200)
    officer_lname = models.CharField(max_length=200)
    officer_email = models.EmailField(max_length=200)
    officer_phone = models.CharField(max_length=200)

    class Meta:
        db_table = 'officer'

    def __str__(self):
        return self.officer_fname


class Guest(models.Model):
    guest_fname = models.CharField(max_length=200)
    guest_lname = models.CharField(max_length=200)
    guest_nickname = models.CharField(max_length=200)
    guest_phonenumber = models.CharField(max_length=200)
    guest_officer = models.CharField(max_length=200)
    guest_email = models.EmailField(max_length=200)
    guest_date = models.DateTimeField("Date login", default=datetime.now())

    class Meta:
        db_table = 'guest'

    def __str__(self):
        return self.guest_fname

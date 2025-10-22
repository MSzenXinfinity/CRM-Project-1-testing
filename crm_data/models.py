from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
	user_id=models.CharField(primary_key=True)
	username=models.OneToOneField(User, on_delete=models.CASCADE)
	address=models.TextField()
	profile_pic=models.ImageField(upload_to='pp')

class Person(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class CallingSheet(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    associate_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name


class Interested(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    associate_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name


class Escalation(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    associate_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()
    payment_explanation = models.TextField()

    def __str__(self):
        return self.name


class PaymentConfirmation(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    associate_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name


class PaymentDone(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    associate_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.name


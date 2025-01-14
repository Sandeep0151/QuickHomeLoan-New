from django.db import models
import random
from django.utils.timezone import now

# Create your models here.


class LoanApplication(models.Model):
    token = models.CharField(max_length=15, unique=True, editable=False)
    required_amount = models.CharField(max_length=255)
    need_time = models.CharField(max_length=50)
    bank_type = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    created_at = models.DateTimeField ( default=now , editable=False )  # Automatically set the creation timestamp

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = f"QHL-{random.randint(10000, 99999)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.mobile})"


class PropertyDetails(models.Model):
    bhk = models.CharField(max_length=10)
    budget = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    city = models.CharField(max_length=100, null=True, blank=True)
    property_name = models.CharField(max_length=100, null=True, blank=True)
    area_pin_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.bhk}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CreditScore(models.Model):
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=50)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    pan = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class ItemType(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5)

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5)

class Currency(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5)
    tc = models.DecimalField(decimal_places=2)

class Provider(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5, blank=True)
    bank_account_name = models.CharField(max_length=50, blank=True)
    bank_account_number = models.CharField(max_length=50, blank=True)

class DocumentType(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    bank_account_name = models.CharField(max_length=50, blank=True)
    bank_account_number = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=75, blank=True)

class TransactionType(models.Model):
    name = models.CharField(max_length=50)
    s_code = models.CharField(max_length=5)

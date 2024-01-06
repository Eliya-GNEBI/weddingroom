from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(AbstractUser):
    pass

class Prestataire(AbstractUser):
    pass

class Salle(models.Model):
    pass

class Reservation(models.Model):
    pass

class Paiement(models.Model):
    pass
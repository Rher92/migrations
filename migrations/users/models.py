from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    class Meta:
        db_table = 'auth_user'

    date_of_birth = models.DateField(null=True, blank=True)
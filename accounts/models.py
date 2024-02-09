from django.contrib.auth.models import AbstractUser
from django.db import models
from company.models import Company


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    my_company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

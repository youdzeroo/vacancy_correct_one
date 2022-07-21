from django.db import models


class Companies(models.Model):
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=40)
    telegram_account = models.CharField(max_length=255, null=True, blank=True)
    skype_account = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.company_name

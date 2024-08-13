from django.db import models

# Create your models here.
class Payment(models.Model):
    bank_used = models.CharField(max_length= 100)
    bank_account_name = models.CharField(max_length= 100)
    date_of_transaction = models.DateField()
    receipt = models.ImageField(upload_to = 'receipt')

    def __str__(self):
        return f'{self.bank_account_name}.{self.bank_used}'

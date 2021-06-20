from django.db import models

# Create your models here.
class user(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(null=True)
    Balance = models.IntegerField(null=True)

    def __str__(self):
        return self.Name

class TransactionHistory(models.Model):
    SenderName = models.CharField(max_length=100, null=True)
    ReceiverName = models.CharField(max_length=100, null=True)
    Amount = models.IntegerField(null=True)
    Date = models.DateField(null=True)

    def __str__(self):
        return self.SenderName + " - " + self.ReceiverName

    
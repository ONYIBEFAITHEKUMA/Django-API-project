from django.db import models
from accounts.models import CustomUser

# Create your models here.

class paymentmethod(models.Model):
    user = models.ForeignKey(CustomUser, related_name='paymentmethod', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, null=True)
    transaction_Id = models.CharField()
    transaction_Refrence = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
 
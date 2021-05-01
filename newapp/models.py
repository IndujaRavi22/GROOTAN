from django.db import models
from django.contrib.auth.models import User

# Create your models here.
PRODUCT_CHOICES=(
    ('TV','tv'),
    ('IPAD','ipad'),
    ('PLAYSTATION','playstation')
)

class Sale(models.Model):
    product=models.CharField( max_length=50,choices=PRODUCT_CHOICES)
    salesman=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    total=models.FloatField(blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product}-{self.quantity}"
    def save(self,*args,**kwargs):
        price=None
        if self.product=='TV':
            price=10000
        elif self.product=='IPAD':
            price=12000
        elif self.product=='PLAYSTATION':
            price=15000
        else:
            pass
        self.total=price*self.quantity
        super().save(*args,**kwargs)


    

    
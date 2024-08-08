from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from store.models import Product

class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    user = models.ForeignKey(User,related_name='orders', on_delete= models.CASCADE, blank=False, null=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=20)
    place = models.CharField(max_length=255)
    phone = models.CharField(validators=[phone_validator], max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ORDERED)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    class Meta:
        ordering = ('-created_at',)

    def get_total_price(self):
        if self.paid:
            return self.paid_amount/100
        
        return 0
    

class OrderItem(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    REJECTED = 'rejected'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (REJECTED, 'Rejected')
    )
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ORDERED)
    shiped_date = models.DateTimeField(null=True)


    def get_total_price(self):
        return self.price / 100 
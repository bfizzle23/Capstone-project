from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    date = models.DateTimeField()
    comment = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return f'{self.name} : {str(self.date)}'

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    featured = models.BooleanField(default=False)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} : {self.price}"
    
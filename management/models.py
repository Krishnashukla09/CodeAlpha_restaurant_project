from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Order(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    table_number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    table_number = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()

from django.db import models
from django.urls import reverse


class Discount(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_item_page', args=[str(self.id)])


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='orders')
    discounts = models.ManyToManyField(Discount, related_name='orders', blank=True)
    taxes = models.ManyToManyField(Tax, related_name='orders', blank=True)

    def __str__(self):
        return 'Заказ под номером: ' + str(self.id)

    def get_absolute_url(self):
        return reverse('get_order_page', args=[str(self.id)])

    def calculate_total(self):
        subtotal = sum(item.price for item in self.items.all())
        discount_amount = sum(discount.amount for discount in self.discounts.all())
        tax_amount = sum(subtotal * (tax.rate / 100) for tax in self.taxes.all())
        total = subtotal - discount_amount + tax_amount
        return total
